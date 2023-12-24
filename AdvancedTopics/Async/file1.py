"""# Chess master Judit Polgár hosts a chess exhibition in which she plays multiple amateur players. She has two ways of conducting the exhibition: synchronously and asynchronously.

# Assumptions:

# 24 opponents
# Judit makes each chess move in 5 seconds
# Opponents each take 55 seconds to make a move
# Games average 30 pair-moves (60 moves total)
# Synchronous version: Judit plays one game at a time, never two at the same time, until the game is complete. Each game takes (55 + 5) * 30 == 1800 seconds, or 30 minutes. The entire exhibition takes 24 * 30 == 720 minutes, or 12 hours.

# Asynchronous version: Judit moves from table to table, making one move at each table. She leaves the table and lets the opponent make their next move during the wait time. One move on all 24 games takes Judit 24 * 5 == 120 seconds, or 2 minutes. The entire exhibition is now cut down to 120 * 30 == 3600 seconds, or just 1 hour. (Source)


import asyncio
import time

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count(), count())


if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
"""


"""
#!/usr/bin/env python3
# countsync.py

import time

def count():
    print("One")
    time.sleep(1)
    print("Two")

def main():
    for _ in range(3):
        count()

if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")



import asyncio


async def fn():
     
    print("one")
    await asyncio.sleep(1)
    await fn2()
    print('four')
    await asyncio.sleep(1)
    print('five')
    await asyncio.sleep(1)
 
async def fn2():
    await asyncio.sleep(1)
    print("two")
    await asyncio.sleep(1)
    print("three")
asyncio.run(fn())




import asyncio
async def fn():
    task=asyncio.create_task(fn2())
    print("one")
    print("four")
    await asyncio.sleep(1)
    print("five")
    await asyncio.sleep(1)
async def fn2():
    print("two")
    await asyncio.sleep(1)
    print("three")

asyncio.run(fn())
"""


import asyncio

async def func1():
    print("Function 1 started")
    await asyncio.sleep(2)
    print("Function 1 ended")

async def func2():
    print("Function 2 started..")
    await asyncio.sleep(5)
    print("Function 2 Ended")

async def func3():
    print("Function 3 started..")
    await asyncio.sleep(1)
    print("Function 3 Ended")

async def main():
    # await func1()
    # await func2()
    # await func3()

    L = await asyncio.gather(
        func1(),
        func2(),
        func3(),
    )
    print("Main Ended...")

asyncio.run(main())