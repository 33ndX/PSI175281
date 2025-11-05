"""Module containing post repository implementation."""

import aiohttp
from typing import Iterable
import json


from lab03.zad1.core.domain.post import Post
from lab03.zad1.core.repositories.ipost import IPostRepository
from lab03.zad1.utils import consts


class PostRepository(IPostRepository):

    async def get_all_posts(self) -> Iterable[Post] | None:
        async with aiohttp.ClientSession() as session:
            async with session.get(consts.API_POSTS_URL) as response:
                if response.status != 200:
                    return None
                json_response = await response.json()
                return [Post(**post) for post in json_response]

    async def filter_posts(self, keywords: str) -> Iterable[Post] | None:
        all_posts = await self.get_all_posts()
        if all_posts is None:
            return None
        filtered_posts = []
        for post in all_posts:
            if keywords.lower() in post.title.lower() or keywords.lower() in post.body.lower():
                filtered_posts.append(post)
        return filtered_posts

    async def post_to_json(self) -> str:
        all_posts = await self.get_all_posts()
        json_post = []
        for post in all_posts:
            json_post.append({
                "userId": post.userId,
                "id": post.id,
                "title": post.title,
                "body": post.body
            })
        return json.dumps(json_post)
