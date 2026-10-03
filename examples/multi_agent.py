import asyncio
from examples.core import bounded_map
async def search_fixture(source):
    await asyncio.sleep(0.01)
    return {'source_id':source,'claim':'Refund period is 14 days.','synthetic':True}
def supported(claim, evidence):
    # Exact fixture comparison, NOT semantic fact checking.
    return any(e['claim'] == claim for e in evidence)
async def main():
    outcomes = await bounded_map(['A','B'],search_fixture,2)
    evidence = [x.value for x in outcomes if not x.error]
    print(evidence)
    print('Unsupported claim rejected:',not supported('Refunds always available.',evidence))
if __name__ == '__main__':
    asyncio.run(main())
