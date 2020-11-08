import threading
import time
import asyncio


async def test(x):
    for i in range(x):
        print(i)
        time.sleep(1)


class ThreadingExample:
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, event: threading.Event, interval=1):
        self.interval = interval
        self.event = event

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True  # Daemonize thread
        thread.start()  # Start the execution

    def run(self):
        loop = asyncio.new_event_loop()
        while True:
            if self.event.is_set():
                break
            print('Doing something imporant in the background')
            loop.run_until_complete(test(5))

            # time.sleep(self.interval)


event = threading.Event()

example = ThreadingExample(event)
print('Checkpoint')
print('This')
time.sleep(4)
event.set()
print('Bye')
