import asyncio

from app.providers.my_provider import MyProvider


class BaseProvider:
    async def get_items(self) -> list[str]:
        items_lists = await asyncio.gather(*[MyProvider().get()])

        from app.models import MyModel

        print("afirst")
        await MyModel.objects.afirst()
        print("afirst done")

        items = [item for items_list in items_lists for item in items_list]

        return items
