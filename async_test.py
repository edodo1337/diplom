import asyncio
import time


async def test(name, x):
    for i in range(x):
        print(name, i)
        # time.sleep(i)
        await asyncio.sleep(1)


task_obj: asyncio.Task = None


async def handler(name, x):
    global task_obj
    if bool(x % 2):
        task_obj = asyncio.create_task(test(name, x))
    else:
        print("Try cancel", task_obj)
        if task_obj is not None:
            print("Cancel", task_obj.cancelled())
            task_obj.cancel()


async def main(loop):
    print("start")
    await handler('A', 7)
    await asyncio.sleep(2)
    await handler('B', 2)
    await asyncio.sleep(2)
    await handler('B', 2)
    await asyncio.sleep(2)
    await handler('C', 9)




loop = asyncio.get_event_loop()

loop.run_until_complete(main(loop))

loop.run_forever()
