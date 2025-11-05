from typing import Iterable

from lab03.zad1.core.domain.post import Post
from lab03.zad1.infrastructure.repositories.postdb import IPostRepository
from lab03.zad1.infrastructure.servicies.ipost import IPostService


class PostService(IPostService):
    repository: IPostRepository

    def __init__(self, repository: IPostRepository) -> None:
        self.repository = repository

    async def get_posts(self) -> Iterable[Post]:
        return await self.repository.get_all_posts()

    async def filter_posts(self, keywords: str) -> Iterable[Post] | None:
        return await self.repository.filter_posts(keywords)

    async def post_to_json(self) -> str:
        return await self.repository.post_to_json()
