from abc import ABC
from typing import Iterable

from lab03_zad2.domains.comment import CommentRecord


class ICommentService(ABC):

    async def get_all_comment(self) -> Iterable[CommentRecord] | None:
        pass

    async def time_cleaning(self, comments: Iterable[CommentRecord]) -> Iterable[CommentRecord] | None:
        pass

    async def filter_comment(self, comments: Iterable[CommentRecord], keywords: str) -> Iterable[CommentRecord] | None:
        pass

    async def sort_by_date(self, comments: Iterable[CommentRecord]) -> Iterable[CommentRecord] | None:
        pass
