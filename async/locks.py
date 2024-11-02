import asyncio
import time

resouece = 0
lock = asyncio.Lock()


async def update_shared_resource():
    global resouece
    async with lock:
        print("before", resouece)
        resouece += 1
        await asyncio.sleep(1)
        print("after", resouece)


async def main():
    now = time.time()
    await asyncio.gather(*(update_shared_resource() for _ in range(5)))
    print(time.time() - now)


loop = asyncio.get_event_loop()
asyncio.ensure_future(main())
try:
    loop.run_until_complete(main())
finally:
    loop.close()
