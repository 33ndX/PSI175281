import random
import aiohttp


from typing import Iterable


from lab03_zad2.repositories.icomment_repository import ICommentRepository, CommentRecord
from lab03_zad2.utils import consts


class CommentRepository(ICommentRepository):

    async def get_all_comment(self) -> Iterable[CommentRecord] | None:
        all_params = await self._get_params()
        parsed_params = await self._parse_params(all_params)
        return parsed_params

    async def time_cleaning(self, comments: Iterable[CommentRecord]) -> Iterable[CommentRecord] | None:
        filtered_comment = []
        for comment in comments:
            if comment.lastUsage < consts.time:
                filtered_comment.append(comment)
        return filtered_comment

    async def filter_comment(self, comments: Iterable[CommentRecord], keywords: str) -> Iterable[CommentRecord] | None:
        filtered_comment = []
        for comment in comments:
            if keywords in comment.name or keywords in comment.body:
                filtered_comment.append(comment)
        return filtered_comment

    async def sort_by_date(self, comments: Iterable[CommentRecord]) -> Iterable[CommentRecord] | None:
        return sorted(comments, key=lambda comment: comment.lastUsage)

    async def _get_params(self) -> Iterable[dict] | None:
        async with aiohttp.ClientSession() as session:
            async with session.get(consts.API_COMMENT_URL) as response:
                if response.status != 200:
                    return None

                return await response.json()

    async def _parse_params(self, params: Iterable[dict]) -> Iterable[CommentRecord]:
        return [CommentRecord(postId=record.get("postId"), id=record.get("id"), name=record.get("name"),
                email=record.get("email"), body=record.get("body"), lastUsage=random.randint(1, 100))
                for record in params]
