import asyncio

async def fetch(delay: int) -> int:
    await asyncio.sleep(delay)
    return 5


async def main() -> None:
    print(await fetch(3))
    print(await fetch(1))
    print(await fetch(5))


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

