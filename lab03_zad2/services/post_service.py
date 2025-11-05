from typing import Iterable

from lab03_zad2.domains.post import PostRecord
from lab03_zad2.repositories.ipost_repository import IPostRepository
from lab03_zad2.services.ipost_service import IPostService


class PostService(IPostService):
    repository: IPostRepository

    def __init__(self, repository: IPostRepository):
        self.repository = repository

    async def get_all_posts(self) -> Iterable[PostRecord] | None:
        return await self.repository.get_all_posts()

    async def time_cleaning(self, posts: Iterable[PostRecord]) -> Iterable[PostRecord] | None:
        return await self.repository.time_cleaning(posts)

    async def filter_posts(self, posts: Iterable[PostRecord], keywords: str) -> Iterable[PostRecord] | None:
        return await self.repository.filter_posts(posts, keywords)

    async def sort_by_date(self, posts: Iterable[PostRecord]) -> Iterable[PostRecord] | None:
        return await self.repository.sort_by_date(posts)
