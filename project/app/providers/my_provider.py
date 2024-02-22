class MyProvider:
    async def get(self) -> list[str]:
        # from app.models import MyModel
        #
        # print("afirst inside gather")
        # await MyModel.objects.afirst()
        # print("afirst inside gather done")

        return ["all ok"]
