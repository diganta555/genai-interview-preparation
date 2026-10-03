import asyncio
from examples.core import retry_read, TransientError
async def main():
    count=0
    async def read():
        nonlocal count
        count+=1
        if count<3:
            raise TransientError('fixture outage')
        return 'success'
    print(await retry_read(read),'attempts:',count)
if __name__ == '__main__':
    asyncio.run(main())
