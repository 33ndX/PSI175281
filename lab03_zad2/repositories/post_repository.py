import aiohttp
import random

from typing import Iterable

from lab03_zad2.repositories.ipost_repository import IPostRepository, PostRecord
from lab03_zad2.utils import consts


class PostRepository(IPostRepository):
    async def get_all_posts(self) -> Iterable[PostRecord] | None:
        all_params = await self._get_params()
        parsed_params = await self._parse_params(all_params)
        return parsed_params

    async def time_cleaning(self, posts: Iterable[PostRecord]) -> Iterable[PostRecord] | None:
        filtered_post = []
        for post in posts:
            if post.lastUsage < consts.time:
                filtered_post.append(post)
        return filtered_post

    async def filter_posts(self, posts: Iterable[PostRecord], keywords: str) -> Iterable[PostRecord] | None:
        filtered_posts = []
        for post in posts:
            if keywords in post.title or keywords in post.body:
                filtered_posts.append(post)
        return filtered_posts

    async def sort_by_date(self, posts: Iterable[PostRecord]) -> Iterable[PostRecord] | None:
        return sorted(posts, key=lambda post: post.lastUsage)

    async def _get_params(self) -> Iterable[dict] | None:
        async with aiohttp.ClientSession() as session:
            async with session.get(consts.API_POST_URL) as response:
                if response.status != 200:
                    return None

                return await response.json()

    async def _parse_params(self, params: Iterable[dict]) -> Iterable[PostRecord] | None:
        return [PostRecord(userId=record.get("userId"), id=record.get("id"), title=record.get("title"),
                           body=record.get("body"), lastUsage=random.randint(1, 100)) for record in params]
