# Chapter 12: Concurrency and Parallelism

import threading
import asyncio

# Thread example
def worker():
    print("Worker thread")

thread = threading.Thread(target=worker)
thread.start()
thread.join()

# Asyncio example
async def main():
    print("Hello async")

asyncio.run(main())