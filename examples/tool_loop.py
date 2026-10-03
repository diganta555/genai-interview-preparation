from examples.core import execute_plan, Identity
if __name__ == '__main__':
    proposal = {'id':'c1','name':'calculator','arguments':{'operation':'add','a':1,'b':2}}
    print(execute_plan([proposal,dict(proposal,id='c2')],Identity('demo','reader')))
