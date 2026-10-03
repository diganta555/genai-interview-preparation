from examples.core import OfflineRAG, demo_documents
if __name__ == '__main__':
    rag = OfflineRAG(demo_documents())
    for question in ('refund receipt','delivery','astronomy quantum'):
        print(question,rag.answer('demo',question))
    print('This is lexical retrieval and extractive answering, not an LLM.')
