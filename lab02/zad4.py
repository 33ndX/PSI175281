import aiohttp
import asyncio

async def fetch(url: str, header:dict) -> str:
    async with aiohttp.ClientSession(headers=header) as session:
        async with session.get(url, data=header) as response:
            return await response.json()

async def main():
    header = {"time": "2025-10-08T20:00"}
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    users = await fetch(url, header)
    print(users)

if __name__ == '__main__':
    asyncio.run(main())