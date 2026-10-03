"""Optional real local embeddings; downloads a model on first execution."""
import os
from sentence_transformers import SentenceTransformer
from examples.core import cosine
if __name__ == '__main__':
    name = os.getenv('EMBEDDING_MODEL','sentence-transformers/all-MiniLM-L6-v2')
    model = SentenceTransformer(name)
    docs = ['A receipt is required for a refund.', 'Delivery takes three working days.']
    vectors = model.encode(docs,normalize_embeddings=True).tolist()
    query = model.encode(['How can I get my money back?'],normalize_embeddings=True)[0].tolist()
    print(sorted(zip(docs,[cosine(query,v) for v in vectors]),key=lambda x:-x[1]))
    print('Evaluate this model on your domain; this is only two demonstration documents.')
