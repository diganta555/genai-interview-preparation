"""Optional LlamaIndex live-model example. Requires configured credentials."""
import os
from llama_index.core import Document, VectorStoreIndex
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
if __name__ == '__main__':
    embed = HuggingFaceEmbedding(model_name=os.environ['EMBEDDING_MODEL'])
    llm = Ollama(model=os.environ['OLLAMA_MODEL'],request_timeout=60.0)
    index = VectorStoreIndex.from_documents([
        Document(text='Refunds require a receipt within 14 days.',metadata={'source':'synthetic-P1'})],
        embed_model=embed)
    response = index.as_query_engine(llm=llm).query('What is the refund policy?')
    print(response)
    print([node.node.metadata for node in response.source_nodes])
