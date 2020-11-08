import asyncio
import time


class async_to_sync:
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        asyncio.get_event_loop().create_task(self.f(*args, **kwargs))


async def test1(x):
    for i in range(x):
        print(i)
        await asyncio.sleep(0.01)


async def test2(x):
    k = 0
    while True:
        if k >= 3:
            break
        print("---", k)
        await asyncio.sleep(0.5)
        k += 1


counter = 0

start = time.time()


async def main(x):
    global counter

    for i in range(x):
        if time.time() - start >= 1:
            break
        # print(i)
        counter += 1
        await asyncio.sleep(0)

    print(counter)


loop = asyncio.get_event_loop()
loop.run_until_complete(main(100000))
