from dependency_injector import containers, providers
from lab03.zad1.infrastructure.repositories.postdb import PostRepository
from lab03.zad1.infrastructure.servicies.post import PostService


class Container(containers.DeclarativeContainer):

    repository = providers.Singleton(
        PostRepository,
    )

    service = providers.Factory(
        PostService,
        repository=repository,
    )
