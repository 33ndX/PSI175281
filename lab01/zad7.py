import asyncio

async def Krojenie() -> None:
    print("Krojenie")
    await asyncio.sleep(2)

async def Gotowanie() -> None:
    print("Gotowanie")
    await asyncio.sleep(5)

async def Samzenie() -> None:
    print("Smażenie")
    await asyncio.sleep(3)

async def Kuchnia() -> None:
    await Krojenie()
    await Gotowanie()
    await Samzenie()

async def main() -> None:
    await Kuchnia()

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    task = loop.create_task(main())

    try:
        loop.run_until_complete(task)
    except KeyboardInterrupt:
        print("Closing the app")

        tasks = asyncio.all_tasks(loop=loop)
        for task_ in tasks:
            task_.cancel()

        group = asyncio.gather(*tasks, return_exceptions=True)
        loop.run_until_complete(group)
        loop.close()


