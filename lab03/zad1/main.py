from dependency_injector.wiring import Provide
import asyncio
from lab03.zad1.container import Container
from lab03.zad1.infrastructure.servicies.ipost import IPostService
import json


async def main( service: IPostService() = Provide[Container.service]) -> None:

    all_post = await service.get_all_posts()

    text = "magnam facilis autem"
    filtered_post = await service.filter_posts(text)

    json_post = await service.post_to_json()

    print(filtered_post)

    with open("post.json", "w") as file:
        json.dump(json.loads(json_post), file, indent=1)
    print("Zapisano do post.json")




if __name__ == '__main__':
    container = Container()
    container.wire(modules=[__name__])

    asyncio.run(main())