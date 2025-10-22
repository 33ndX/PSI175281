import aiohttp
import asyncio

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
             content = await response.read()
             return content

async def save_content(url: str, path: str) -> None:
    content = await fetch(url)
    with open(path, 'wb') as f:
        f.write(content)

async def main() -> None:
    url = 'https://ichef.bbci.co.uk/ace/standard/976/cpsprodpb/cea1/live/1de105b0-f5a5-11ef-bcea-7b70a14a5556.jpg'
    path = r"D:/175281/lab01/plik.jpg"
    await save_content(url, path)


if __name__ == '__main__':
    asyncio.run(main())