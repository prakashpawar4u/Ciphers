import time
import asyncio
import requests

async def function1():
    await asyncio.sleep(1)
    print("func 1")
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("icon.ico","wb").write(response.content)

async def function2():
    await asyncio.sleep(3)
    print("func 2")

async def function3():
    await asyncio.sleep(4)
    print("func 3")

async def main():
    l = await asyncio.gather(
        function1(),
        function2(),
        function3()

    )

    # task = asyncio.create_task(function1())
    await function1()
    await function2()
    await function3()
asyncio.run(main())