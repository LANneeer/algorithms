import asyncio
import time


async def set_future_task(future, value):
    await asyncio.sleep(3)
    future.set_result(value)
    print(value)


async def main():
    now = time.time()
    loop = asyncio.get_running_loop()
    future = loop.create_future()

    asyncio.create_task(set_future_task(future, "Future ready"))
    result = await future
    print(result)
    print(time.time() - now)


asyncio.run(main())
