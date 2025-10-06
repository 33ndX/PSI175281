import asyncio

async def maszynaA() -> None:
    czas = 0
    while czas < 15:
        print("maszyna A")
        await asyncio.sleep(2)
        czas += 2

async def maszynaB() -> None:
    czas = 0
    while czas < 15:
        print("maszyna B")
        await asyncio.sleep(3)
        czas += 3

async def maszynaC() -> None:
    czas = 0
    while czas < 15:
        print("maszyna C")
        await asyncio.sleep(5)
        czas += 5

async def harmonogram() -> None:
    await asyncio.gather(maszynaA(), maszynaB(), maszynaC())

async def main() -> None:
    await harmonogram()

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())




