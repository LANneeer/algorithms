import asyncio
import time


async def fetch(id, time):
    await asyncio.sleep(time)
    return id


async def non_concurrently():
    now = time.time()
    task1 = fetch(1, 2)
    task2 = fetch(2, 3)
    task3 = fetch(3, 1)

    result1 = await task1
    result2 = await task2
    result3 = await task3
    print(result1, result2, result3)
    print(time.time() - now)


async def concurrently1():
    now = time.time()
    task1 = asyncio.create_task(fetch(1, 2))
    task2 = asyncio.create_task(fetch(2, 3))
    task3 = asyncio.create_task(fetch(3, 1))

    result1 = await task1
    result2 = await task2
    result3 = await task3
    print(result1, result2, result3)
    print(time.time() - now)


async def concurrently2():
    now = time.time()
    results = await asyncio.gather(fetch(1, 2), fetch(2, 3), fetch(3, 1))
    print(results)
    print(time.time() - now)


# async def concurrently3():
#     now = time.time()
#     results = []
#     async with asyncio.TaskGroup() as tg:
#         for id, t in enumerate([2, 3, 1], start=1):
#             task = tg.create_task(fetch(id, t))
#             results.append(task)
#     results = [task.result() for task in results]
#     print(results)
#     print(time.time() - now)


asyncio.run(non_concurrently())
asyncio.run(concurrently1())
asyncio.run(concurrently2())
# asyncio.run(concurrently3())
