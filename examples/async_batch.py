import asyncio, time
from examples.core import bounded_map
async def work(item):
    await asyncio.sleep(0.01)
    if item == 17:
        raise ValueError('synthetic bad record')
    return item * 2
async def main():
    for concurrency in (1, 5, 10):
        start = time.perf_counter()
        results = await bounded_map(range(100), work, concurrency)
        print(concurrency, round(time.perf_counter()-start, 3),
              'seconds; failures:', sum(x.error is not None for x in results))
if __name__ == '__main__':
    asyncio.run(main())
