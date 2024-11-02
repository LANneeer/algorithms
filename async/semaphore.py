import asyncio
import time


async def open_resounce_connection(semaphore, resouce):
    async with semaphore:
        print("open connection for", resouce)
        await asyncio.sleep(1)
        print("close connection for", resouce)


async def main():
    now = time.time()
    semaphore = asyncio.Semaphore(2)
    await asyncio.gather(*[open_resounce_connection(semaphore, i) for i in range(1, 9)])
    print(time.time() - now)


asyncio.run(main())
