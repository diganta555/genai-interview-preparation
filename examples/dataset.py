import json
from pathlib import Path
def validate(records):
    seen = set()
    for row in records:
        if set(row) != {'id','group','input','output'} or not all(isinstance(x,str) and x for x in row.values()):
            raise ValueError('invalid record')
        pair = (row['input'],row['output'])
        if pair in seen:
            raise ValueError('duplicate pair')
        seen.add(pair)
if __name__ == '__main__':
    rows = [{'id':str(i),'group':'train' if i<16 else 'test',
             'input':f'Extract amount from synthetic invoice {i}: INR {100+i}',
             'output':json.dumps({'currency':'INR','amount':100+i})} for i in range(20)]
    validate(rows)
    print('Validated synthetic records:',len(rows),'held out:',sum(r['group']=='test' for r in rows))
