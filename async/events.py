import asyncio
import time


async def waiter(event):
    print("waiting")
    await event.wait()
    print("continue")


async def setter(event):
    await asyncio.sleep(1)
    event.set()
    print("event has been sent")


async def main():
    now = time.time()
    event = asyncio.Event()
    await asyncio.gather(waiter(event), setter(event))
    print(time.time() - now)


asyncio.run(main())
