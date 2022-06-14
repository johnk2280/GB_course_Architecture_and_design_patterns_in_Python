from framework.abstracts.abstract_view import View
from framework.response import Response

from logger import LOGGER


class PageNotFound404View(View):

    def get(self, request, *args, **kwargs) -> Response:
        return Response(status='404 Page Not Found', body='404.html')


class MethodNotAllowedView(View):
    def get(self, request, *args, **kwargs) -> Response:
        return Response(status='405 Method Not Allowed', body='405.html')


class IndexView(View):

    def get(self, request, *args, **kwargs) -> Response:
        return Response(body='index.html')


class AboutView(View):

    def get(self, request, *args, **kwargs) -> Response:
        return Response(body='about.html')


class ContactView(View):

    logger = LOGGER

    def get(self, request, *args, **kwargs) -> Response:
        return Response(body='contacts.html')

    def post(self, request, *args, **kwargs) -> Response:
        self.logger.debug('Data: %s', request.body)
        return Response(body='contacts.html')
