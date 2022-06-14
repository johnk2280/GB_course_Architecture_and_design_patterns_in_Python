from abc import ABC

from framework.response import Response


class View(ABC):

    def get(self, request, *args, **kwargs) -> Response:
        return Response(status='405 Method Not Allowed', body='405.html')

    def post(self, request, *args, **kwargs) -> Response:
        return Response(status='405 Method Not Allowed', body='405.html')

    def put(self, request, *args, **kwargs) -> Response:
        return Response(status='405 Method Not Allowed', body='405.html')

    def delete(self, request, *args, **kwargs) -> Response:
        return Response(status='405 Method Not Allowed', body='405.html')

    def update(self, request, *args, **kwargs) -> Response:
        return Response(status='405 Method Not Allowed', body='405.html')


class ListView(ABC):
    pass
