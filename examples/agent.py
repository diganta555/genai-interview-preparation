from examples.core import execute_plan, Identity
if __name__ == '__main__':
    proposals = [{'id':str(i),'name':'calculator',
                  'arguments':{'operation':'add','a':i,'b':1}} for i in range(10)]
    print(execute_plan(proposals,Identity('demo','reader'),limit=3))
    print('Fixed proposal fixture. Replace proposal generation with a model adapter.')
