import aiohttp
import asyncio
import time

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def get_temp(url: str, hour=(time.gmtime()).tm_hour ) -> int:
    response = await fetch(url)
    time = (response.get("hourly"))
    temp = time.get("temperature_2m")
    return temp[hour]

async def temp_data(city: dict) -> dict:
    response = {}
    for name, loc in city.items():
        response.update({name: await get_temp(f"https://api.open-meteo.com/v1/forecast?latitude={loc.get('latitude')}&longitude={loc.get('longitude')}&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")})
    return response

async def main():
    miasta = {
        "Porlamar": {"latitude": 10.95796, "longitude": -63.84906},
        "Moroni": {"latitude": -11.749997, "longitude": 43.1999992},
        "Helsinki": {"latitude": 60.16952, "longitude": 24.93545}
    }
    temperatury = await temp_data(miasta)
    print(temperatury)






if __name__ == '__main__':
    asyncio.run(main())