from abc import ABC

from framework.response import Response


class View(ABC):

    def get(self, request, *args, **kwargs) -> Response:
        pass

    def post(self, request, *args, **kwargs) -> Response:
        pass

    def put(self, request, *args, **kwargs) -> Response:
        pass

    def delete(self, request, *args, **kwargs) -> Response:
        pass

    def update(self, request, *args, **kwargs) -> Response:
        pass

