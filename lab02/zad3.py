import aiohttp
import asyncio

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text(encoding='utf-8')

async def multifetch(urls: list[str]) -> None:
    multi = await asyncio.gather(fetch(urls[0]), fetch(urls[1]), fetch(urls[2]), fetch(urls[3]), fetch(urls[4]))
    print(multi)

async def main():
    urls = ['https://www.python.org/dev/peps/pep',
            'https://wmii.uwm.edu.pl/', 'https://www.iracing.com/',
            'https://store.steampowered.com/app/266410/iRacing/',
            'https://www.top500.org/lists/top500/list/2023/11/']
    await multifetch(urls)

if __name__ == '__main__':
    asyncio.run(main())
