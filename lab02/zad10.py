import asyncio
import aiohttp
import datetime

async def fetch(url: str) -> str:
    for i in range(3):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()

async def download(url: str) -> str:
    hour = datetime.datetime.now().hour
    url = "https://api.open-meteo.com/v1/forecast?latitude=49.299&longitude=19.9489&hourly=temperature_2m&forecast_days=1"
    response = await fetch(url)
    time = (response.get("hourly"))
    temp = time.get("temperature_2m")
    return temp[hour]

async def save(url: str) -> None:
    file = open('plik.txt', 'a')
    file.write(f"Zakopane temperatura: {await download(url)}\n")
    file.close()

async def main():
    await save("https://api.open-meteo.com/v1/forecast?latitude=49.299&longitude=19.9489&hourly=temperature_2m&forecast_days=1")

if __name__ == '__main__':
    asyncio.run(main())