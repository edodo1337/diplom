import asyncio
import time


async def test(name, x, event):
    for i in range(x):
        print(name, i)
        if event.is_set():
            break
        # time.sleep(i)
        await asyncio.sleep(1)


task_obj: asyncio.Task = None


async def handler(name, x, event):
    global task_obj
    if bool(x % 2):
        task_obj = asyncio.create_task(test(name, x, event))
    else:
        event.set()
        print("Try cancel", task_obj.cancelled())
        # if task_obj is not None:
        #     print("Cancel", task_obj.cancelled())
        #     task_obj.cancel()


async def main(loop):
    print("start")
    event = asyncio.Event()

    await handler('A', 17, event)
    await asyncio.sleep(2)
    await handler('B', 2, event)
    print(task_obj.cancelled())
    await asyncio.sleep(2)
    print("DONE", event.is_set(), task_obj.cancelled(), task_obj.done())


    # await handler('B', 2)
    # await asyncio.sleep(2)
    # await handler('C', 9)


loop = asyncio.get_event_loop()

loop.run_until_complete(main(loop))

loop.run_forever()

# from tqdm import tqdm
# from loguru import logger
# import time
#
# logger.remove()
# logger.add(lambda msg: tqdm.write(msg, end=""))
#
# logger.info("Initializing")

for x in tqdm(range(100)):
    # logger.info("Iterating #{}", x)
    time.sleep(0.1)
