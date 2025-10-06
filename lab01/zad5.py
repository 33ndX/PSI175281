import asyncio

async def fibonacci(n) -> None:
    x, y = 0, 1
    for i in range(1, n+1):
        print(x)
        await asyncio.sleep(1)
        x, y = x+y, x





if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    task=loop.create_task(fibonacci(5))
    loop.run_until_complete(task)

    try:
        loop.run_until_complete(task)  # 3
    except KeyboardInterrupt:  # 4
        print("Closing the app")

        tasks = asyncio.all_tasks(loop=loop)  # 5
        for task_ in tasks:
            task_.cancel()

        group = asyncio.gather(*tasks, return_exceptions=True)
        loop.run_until_complete(group)
        loop.close()