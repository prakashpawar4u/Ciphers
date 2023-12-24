from asyncio import futures
import threading
import time
import inspect
from concurrent.futures import ThreadPoolExecutor

def func(secs):
    print(f"Sleeping for {secs}")
    time.sleep(secs)
    return(f"{inspect.stack()[0][3]}slept for {secs}")

def main():
    time1 = time.perf_counter()
    #Normal code
    func(2)
    func(5)
    func(1)

    #Threaded code
    # t1 = threading.Thread(target=func, args=[2])
    # t2 = threading.Thread(target=func, args=[2])
    # t3 = threading.Thread(target=func, args=[1]
    # )
    # t1.start()
    # t2.start()
    # t3.start()

    # t1.join()
    # t2.join()
    # t3.join()
    time2 = time.perf_counter()
    print(f"timetaken :: {time2-time1}")


def pooling_func():
    with ThreadPoolExecutor(max_workers=1) as executor:
        # future1 = executor.submit(func,4)
        # future2 = executor.submit(func,2)
        # future3 = executor.submit(func,4)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())

        l =[4,2,3]
        results = executor.map(func, l)
        for result in results:
            print(result)

pooling_func()