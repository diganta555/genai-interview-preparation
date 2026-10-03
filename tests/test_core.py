import asyncio
from decimal import Decimal
import math
import sqlite3
import unittest
from examples.core import (cosine, chunks, VectorStore, Record, OfflineRAG, demo_documents,
    bounded_map, classification_metrics, retrieval_metrics, calculate, execute_tool,
    execute_plan, Identity, fictional_cost, PreferenceMemory, retry_read, TransientError,
    rrf, cache_key)
from examples.sql import customers
from examples.evaluate import run

class VectorTests(unittest.TestCase):
    def test_geometry(self):
        self.assertAlmostEqual(cosine([1,0],[1,0]),1)
        self.assertAlmostEqual(cosine([1,0],[0,1]),0)
        self.assertAlmostEqual(cosine([1,0],[-1,0]),-1)
    def test_invalid(self):
        for a,b in [([],[]),([1],[1,2]),([0],[1]),([math.nan],[1]),([math.inf],[1])]:
            with self.assertRaises(ValueError): cosine(a,b)
    def test_large_finite(self):
        self.assertAlmostEqual(cosine([1e200,1e200],[1e200,1e200]),1)
    def test_chunks_offsets(self):
        self.assertEqual(chunks('abcdefghij',4,1),[(0,'abcd'),(3,'defg'),(6,'ghij')])
        self.assertEqual(chunks('',4,1),[])
        self.assertEqual(chunks('a',4,1),[(0,'a')])
    def test_chunk_invalid(self):
        for size,overlap in [(0,0),(4,4),(4,-1)]:
            with self.assertRaises(ValueError): chunks('x',size,overlap)
    def test_same_id_two_tenants(self):
        store=VectorStore(2)
        store.upsert(Record('same','A','s','v1','A text',(1,0)))
        store.upsert(Record('same','B','s','v1','B text',(1,0)))
        self.assertEqual(store.search('A',[1,0])[0][1].text,'A text')
        self.assertEqual(len(store.records('B')),1)
    def test_update_delete(self):
        store=VectorStore(2)
        store.upsert(Record('1','A','s','v1','old',(1,0)))
        store.upsert(Record('1','A','s','v2','new',(0,1)))
        self.assertEqual(store.search('A',[0,1])[0][1].version,'v2')
        self.assertTrue(store.delete('A','1'))
        self.assertFalse(store.delete('A','1'))
    def test_replacement_removes_orphans(self):
        store=VectorStore(2)
        store.upsert(Record('1','A','s','v1','one',(1,0)))
        store.upsert(Record('2','A','s','v1','two',(0,1)))
        store.replace_source('A','s',[Record('3','A','s','v2','three',(1,1))])
        self.assertEqual([r.id for r in store.records('A')],['3'])
    def test_replacement_validates_before_mutation(self):
        store=VectorStore(2)
        store.upsert(Record('1','A','s','v1','one',(1,0)))
        with self.assertRaises(ValueError):
            store.replace_source('A','s',[Record('2','B','s','v2','bad',(1,0))])
        self.assertEqual(len(store.records('A')),1)
    def test_zero_and_dimension_rejected(self):
        store=VectorStore(2)
        for vector in [(0,0),(1,)]:
            with self.assertRaises(ValueError): store.upsert(Record('1','A','s','v1','text',vector))

class RagTests(unittest.TestCase):
    def setUp(self): self.rag=OfflineRAG(demo_documents())
    def test_support_and_citation(self):
        result=self.rag.answer('demo','refund receipt')
        self.assertIn('14 days',result['answer'])
        self.assertEqual(result['citations'][0]['source_id'],'refund-policy')
    def test_abstention(self):
        self.assertTrue(self.rag.answer('demo','astronomy quantum')['abstained'])
    def test_no_tenant_leak(self):
        ids={r.source_id for _,r in self.rag.retrieve('demo','private refunds policy')}
        self.assertNotIn('private-policy',ids)
        self.assertTrue(self.rag.answer('missing','refund')['abstained'])
    def test_document_version_update(self):
        self.rag.ingest('demo','refund-policy','v2','Refunds require a receipt.')
        result=self.rag.answer('demo','refund receipt')
        self.assertEqual(result['citations'][0]['version'],'v2')
        self.assertNotIn('14 days',result['answer'])
    def test_evaluation_boundary(self):
        result=run()
        self.assertEqual(len(result),4)
        self.assertTrue(all(x['abstention_pass'] for x in result))
        self.assertTrue(all(x['semantic_review']=='not performed' for x in result))

class ToolTests(unittest.TestCase):
    def test_calculator(self): self.assertEqual(calculate('multiply',12,7),84)
    def test_calculator_bad(self):
        for op,a,b in [('divide',1,0),('eval',1,2),('add',math.inf,1)]:
            with self.assertRaises(ValueError): calculate(op,a,b)
    def test_permission_and_unknown(self):
        for proposal in [
            {'id':'1','name':'employee','arguments':{'employee_id':'E1'}},
            {'id':'2','name':'shell','arguments':{}}]:
            with self.assertRaises(PermissionError): execute_tool(proposal,Identity('demo','reader'))
    def test_call_id(self):
        result=execute_tool({'id':'call-X','name':'calculator',
            'arguments':{'operation':'add','a':1,'b':2}},Identity('demo','reader'))
        self.assertEqual(result,{'tool_call_id':'call-X','result':3})
    def test_extra_args(self):
        with self.assertRaises(ValueError):
            execute_tool({'id':'1','name':'calculator',
                'arguments':{'operation':'add','a':1,'b':2,'tenant':'other'}},Identity('demo','reader'))
    def test_no_progress(self):
        p={'id':'1','name':'calculator','arguments':{'operation':'add','a':1,'b':2}}
        self.assertEqual(execute_plan([p,p],Identity('demo','reader'))['stop_reason'],'no_progress')
    def test_budget(self):
        ps=[{'id':str(i),'name':'calculator','arguments':{'operation':'add','a':i,'b':1}} for i in range(5)]
        self.assertEqual(execute_plan(ps,Identity('demo','reader'),2)['stop_reason'],'budget')

class MetricAndStateTests(unittest.TestCase):
    def test_imbalance(self):
        m=classification_metrics(0,0,10,990)
        self.assertEqual(m['accuracy'],0.99)
        self.assertEqual(m['recall'],0)
    def test_retrieval_duplicates(self):
        self.assertEqual(retrieval_metrics(['A','A','B'],{'B'},2),
                         {'recall_at_k':1.0,'reciprocal_rank_at_k':0.5})
    def test_rrf(self):
        self.assertEqual(rrf([['A','B'],['B','A']])[0][0],'A')
        self.assertEqual(rrf([['A','A']]),rrf([['A']]))
    def test_cost(self):
        self.assertEqual(fictional_cost(1_000_000,1_000_000),Decimal('10'))
        with self.assertRaises(ValueError): fictional_cost(-1,2)
    def test_cache_identity_version(self):
        a=cache_key(Identity('A','reader'),'q','i1','p1','m','acl1')
        b=cache_key(Identity('B','reader'),'q','i1','p1','m','acl1')
        c=cache_key(Identity('A','reader'),'q','i1','p1','m','acl2')
        self.assertNotEqual(a,b)
        self.assertNotEqual(a,c)
    def test_memory_scope_expiry_update(self):
        memory=PreferenceMemory()
        memory.put('A','u','k','old',10,now=1)
        memory.put('A','u','k','new',10,now=2)
        self.assertEqual(memory.get('A','u','k',now=3),'new')
        self.assertIsNone(memory.get('B','u','k',now=3))
        self.assertIsNone(memory.get('A','u','k',now=13))
    def test_memory_delete(self):
        memory=PreferenceMemory()
        memory.put('A','u','k','v',10,now=1)
        memory.delete('A','u','k')
        self.assertIsNone(memory.get('A','u','k',now=2))
    def test_sql_scope_threshold_status(self):
        with sqlite3.connect(':memory:') as conn:
            conn.execute('CREATE TABLE orders(tenant TEXT, customer_id TEXT, amount_paise INTEGER, purchased_on TEXT, status TEXT)')
            conn.executemany('INSERT INTO orders VALUES(?,?,?,?,?)',[
                ('A','C1',6000000,'2026-06-01','paid'),('A','C1',5000000,'2026-07-01','paid'),
                ('A','C2',10000000,'2026-07-01','paid'),('B','C3',90000000,'2026-07-01','paid'),
                ('A','C4',90000000,'2026-07-01','canceled'),('A','C5',90000000,'2026-01-01','paid')])
            self.assertEqual(customers(conn,'A','2026-04-03'),[('C1',11000000)])

class AsyncTests(unittest.IsolatedAsyncioTestCase):
    async def test_bounded_active_and_order(self):
        active=peak=0
        async def work(i):
            nonlocal active,peak
            active+=1
            peak=max(peak,active)
            try:
                await asyncio.sleep(0.001)
                return i*2
            finally: active-=1
        result=await bounded_map(range(20),work,3)
        self.assertLessEqual(peak,3)
        self.assertEqual([x.value for x in result],list(range(0,40,2)))
    async def test_error_and_timeout_preserved(self):
        async def work(i):
            if i==1: raise ValueError('bad')
            if i==2: await asyncio.sleep(0.1)
            return i
        result=await bounded_map(range(3),work,2,timeout=0.01)
        self.assertEqual(result[0].value,0)
        self.assertEqual(result[1].error,'ValueError')
        self.assertEqual(result[2].error,'TimeoutError')
    async def test_cancellation_cleanup(self):
        active=0
        started=asyncio.Event()
        async def work(i):
            nonlocal active
            active+=1
            started.set()
            try: await asyncio.sleep(10)
            finally: active-=1
        task=asyncio.create_task(bounded_map(range(10),work,2,timeout=20))
        await started.wait()
        task.cancel()
        with self.assertRaises(asyncio.CancelledError): await task
        self.assertEqual(active,0)
    async def test_retry_transient_only(self):
        calls=0
        async def work():
            nonlocal calls
            calls+=1
            if calls<2: raise TransientError()
            return 'ok'
        self.assertEqual(await retry_read(work),'ok')
        self.assertEqual(calls,2)
        calls=0
        async def permanent():
            nonlocal calls
            calls+=1
            raise PermissionError()
        with self.assertRaises(PermissionError): await retry_read(permanent)
        self.assertEqual(calls,1)
    async def test_retry_attempt_cap(self):
        calls=0
        async def bad():
            nonlocal calls
            calls+=1
            raise TransientError()
        with self.assertRaises(TransientError): await retry_read(bad,attempts=2)
        self.assertEqual(calls,2)

if __name__=='__main__': unittest.main()
