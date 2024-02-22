from asgiref.sync import async_to_sync
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.providers.base import BaseProvider


class MyView(APIView):
    @async_to_sync
    async def get(self, request) -> Response:
        items = await BaseProvider().get_items()

        search_items_response = {'items': items}

        return Response(search_items_response, status=status.HTTP_200_OK)
