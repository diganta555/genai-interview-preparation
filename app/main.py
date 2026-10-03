"""Development reference only. In-memory lexical/extractive RAG, not production."""
import asyncio
import os
import secrets
import time
from typing import Annotated
from fastapi import FastAPI, Header, HTTPException, Depends
from pydantic import BaseModel, ConfigDict, Field
from examples.core import OfflineRAG, demo_documents, Identity

app=FastAPI(title='GenAI Learning API',version='0.1.0')
rag=OfflineRAG(demo_documents())
lock=asyncio.Lock()
class QueryRequest(BaseModel):
    model_config=ConfigDict(extra='forbid')
    question: str=Field(min_length=1,max_length=2000)
class SourceRequest(BaseModel):
    model_config=ConfigDict(extra='forbid')
    source_id: str=Field(min_length=1,max_length=100,pattern=r'^[a-zA-Z0-9_-]+$')
    version: str=Field(min_length=1,max_length=100)
    text: str=Field(min_length=1,max_length=10000)

def identity(authorization: Annotated[str|None,Header()]=None) -> Identity:
    expected=os.getenv('DEMO_API_KEY')
    if not expected:
        raise HTTPException(503,'Development API key is not configured')
    if not authorization or not secrets.compare_digest(authorization,'Bearer '+expected):
        raise HTTPException(401,'Invalid development credential')
    # One configured development identity. Replace with real token verification.
    return Identity('demo','reader')

@app.get('/health')
def health():
    return {'status':'ok','mode':'offline-lexical-extractive','persistence':'memory'}

@app.post('/query')
async def query(request: QueryRequest, principal: Annotated[Identity,Depends(identity)]):
    if not request.question.strip():
        raise HTTPException(422,'Question is blank')
    start=time.perf_counter()
    async with lock:
        result=rag.answer(principal.tenant,request.question)
    return {**result,'latency_ms':(time.perf_counter()-start)*1000}

@app.post('/sources',status_code=201)
async def source(request: SourceRequest, principal: Annotated[Identity,Depends(identity)]):
    # Local lab permits ingestion for this fixed identity. Production needs roles.
    async with lock:
        rag.ingest(principal.tenant,request.source_id,request.version,request.text)
        count=sum(r.source_id==request.source_id for r in rag.store.records(principal.tenant))
    return {'source_id':request.source_id,'version':request.version,'chunks':count,
            'warning':'Fixed lexical vocabulary; unknown words are not indexed. Data resets on restart.'}
