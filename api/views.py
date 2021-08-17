from typing import Generic
from rest_framework import generics
from rest_framework.response import Response


class HelloWorld(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        return Response("Hello world")
