from examples.core import Record, VectorStore
if __name__ == '__main__':
    store = VectorStore(2)
    store.upsert(Record('1','demo','source','v1','Old text',(1,0)))
    print('Embeddings:', [r.vector for r in store.records('demo')])
    store.upsert(Record('1','demo','source','v2','Updated text',(0,1)))
    print('Updated:',store.search('demo',[0,1]))
    print('Other tenant:',store.search('other',[0,1]))
    store.delete('demo','1')
    print('After delete:',store.records('demo'))
