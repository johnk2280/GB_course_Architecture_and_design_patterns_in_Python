from abc import ABC

from framework.abstracts.abstract_model import Model
from framework.response import Response
from logger import LOGGER


class View(ABC):

    logger = LOGGER

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
    model: Model = None

    def get_queryset(self):
        return self.model.get_all()
