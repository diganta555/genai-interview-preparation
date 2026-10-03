from examples.core import Identity, execute_plan, OfflineRAG, demo_documents
if __name__ == '__main__':
    attack={'id':'attack','name':'upload_confidential_files','arguments':{'url':'https://invalid.example'}}
    print('Denied tool:',execute_plan([attack],Identity('demo','reader')))
    rag=OfflineRAG(demo_documents())
    print('Authorized source IDs:',[r.source_id for _,r in rag.retrieve('demo','private refunds policy')])
    print('No model injection detector is claimed; permissions are enforced in code.')
