from examples.core import execute_tool, Identity
if __name__ == '__main__':
    proposal = {'id':'call-1','name':'calculator',
                'arguments':{'operation':'multiply','a':12,'b':7}}
    print(execute_tool(proposal,Identity('demo','reader')))
