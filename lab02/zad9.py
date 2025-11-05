import asyncio
import aiohttp

async def fetch(url: str) -> str:
    for i in range(3):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                status = response.status

                if status in range(200, 300):
                    print("Status:", status)
                    #return response
                elif status in range(500, 600):
                    print("Status:", status)
                    continue
                else:
                    return None
    return None

async def main():
    url = "https://api.open-meteo.com/v1/forecast?latitude=10.95796&longitude=-63.84906&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    tasks = [fetch(url) for i in range(100)]
    result = await asyncio.gather(*tasks)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())