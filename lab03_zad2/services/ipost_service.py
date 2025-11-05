from abc import ABC
from typing import Iterable

from lab03_zad2.domains.post import PostRecord


class IPostService(ABC):

    async def get_all_posts(self) -> Iterable[PostRecord] | None:
        pass

    async def time_cleaning(self, posts: Iterable[PostRecord]) -> Iterable[PostRecord] | None:
        pass

    async def filter_posts(self, posts: Iterable[PostRecord], keywords: str) -> Iterable[PostRecord] | None:
        pass

    async def sort_by_date(self, posts: Iterable[PostRecord]) -> Iterable[PostRecord] | None:
        pass
