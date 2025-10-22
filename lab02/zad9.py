from urllib import response

import aiohttp
import asyncio


async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get() as response:
            if response.status in range(200, 299):
                return await response
            elif response.status :





if __name__ == '__main__':
    asyncio.run(main())


