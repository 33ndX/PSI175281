import aiohttp
import asyncio
import time

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def get_zakopane_temp(hour=(time.gmtime()).tm_hour) -> str:
    url = "https://api.open-meteo.com/v1/forecast?latitude=49.299&longitude=19.9489&hourly=temperature_2m&forecast_days=1"
    response = await fetch(url)
    time = (response.get("hourly"))
    temp = time.get("temperature_2m")
    return temp[hour]
async def main():

    print(await get_zakopane_temp())

if __name__ == '__main__':
    asyncio.run(main())