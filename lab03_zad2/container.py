from dependency_injector import containers, providers

from lab03_zad2.services.post_service import PostService
from repositories.post_repository import PostRepository
from services.comment_service import CommentService
from repositories.comment_repository import CommentRepository


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    post_repository = providers.Singleton(PostRepository)
    comment_repository = providers.Singleton(CommentRepository)

    post_service = providers.Factory(
        PostService,
        repository=post_repository
    )

    comment_service = providers.Factory(
        CommentService,
        repository=comment_repository
    )
