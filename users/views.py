from rest_framework.views import APIView
from rest_framework.response import Response


class UserView(APIView):
    def get(self, *args, **kwargs):
        return Response('Hello')

    def post(self, *args, **kwargs):
        return Response('Hello')

    def put(self, *args, **kwargs):
        return Response('Hello')

    def patch(self, *args, **kwargs):
        return Response('Hello')

    def delete(self, *args, **kwargs):
        return Response('Hello')
