from abc import ABC
from typing import Iterable
from lab03.zad1.core.domain.post import Post


class IPostService(ABC):


    async def get_all_posts(self) -> Iterable[Post] | None:
        pass


    async def filter_posts(self, keywords: str) -> Iterable[Post] | None:
        pass


    async def post_to_json(self) -> str:
        pass
