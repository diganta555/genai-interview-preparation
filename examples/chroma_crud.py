"""Optional Chroma CRUD with explicit vectors; no implicit embedding download."""
import tempfile
import chromadb
if __name__ == '__main__':
    with tempfile.TemporaryDirectory() as path:
        client = chromadb.PersistentClient(path=path)
        collection = client.create_collection('demo',embedding_function=None)
        collection.add(ids=['D1'],documents=['Original'],embeddings=[[1.0,0.0]],
                       metadatas=[{'tenant':'demo','version':'v1'}])
        print(collection.get(include=['embeddings','documents','metadatas']))
        collection.update(ids=['D1'],documents=['Updated'],embeddings=[[0.0,1.0]],
                          metadatas=[{'tenant':'demo','version':'v2'}])
        print(collection.query(query_embeddings=[[0.0,1.0]],n_results=1,
                               where={'tenant':'demo'}))
        collection.delete(ids=['D1'])
        print('After deletion:',collection.count())
