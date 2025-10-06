import asyncio


async def fun1() -> None:
    await asyncio.sleep(3)
    print("Hello")

async def fun2() -> None:
    await asyncio.sleep(1)
    print("World")

async def main() -> None:
    await asyncio.gather(fun1(), fun2())



if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())