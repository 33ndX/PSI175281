from typing import Iterable

from lab03_zad2.domains.comment import CommentRecord
from lab03_zad2.repositories.icomment_repository import ICommentRepository
from lab03_zad2.services.icomment_service import ICommentService


class CommentService(ICommentService):
    repository: ICommentRepository

    def __init__(self, repository: ICommentRepository) -> None:
        self.repository = repository

    async def get_all_comment(self) -> Iterable[CommentRecord] | None:
        return await self.repository.get_all_comment()

    async def time_cleaning(self, comments: Iterable[CommentRecord]) -> Iterable[CommentRecord] | None:
        return await self.repository.time_cleaning(comments)

    async def filter_comment(self, comments: Iterable[CommentRecord], keywords: str) -> Iterable[CommentRecord] | None:
        return await self.repository.filter_comment(comments, keywords)

    async def sort_by_date(self, comments: Iterable[CommentRecord]) -> Iterable[CommentRecord] | None:
        return await self.repository.sort_by_date(comments)
