from .response import Response
from .request import Request
from .views import MethodNotAllowedView
from .views import PageNotFound404View
from .views import View

from logger import LOGGER


class Framework:

    logger = LOGGER

    def __init__(self, urls: dict):
        self.urls = urls
        self._not_found_view = PageNotFound404View
        self._not_allowed_view = MethodNotAllowedView

    def __call__(self, environ: dict, start_response: callable):
        # self.logger.info('Request received: %s', environ)
        request = Request(environ)
        view = self._get_view(request)
        response = self._get_response(request, view)
        start_response(response.status, list(response.headers.items()))
        return [response.body.encode()]

    def _get_view(self, request: Request) -> View:
        try:
            return self.urls[request.path]
        except KeyError as e:
            self.logger.debug('Page not found.')
            self.logger.exception(e)
            return self._not_found_view
        except AttributeError as e:
            self.logger.debug('Method not allowed.')
            self.logger.exception(e)
            return self._not_allowed_view

    def _get_response(self, request: Request, view: View) -> Response:
        try:
            self.logger.debug('view = %s', view)
            return getattr(view, request.method)(view, request)
        except AttributeError as e:
            self.logger.exception(e)
            self.logger.debug('Method not allowed.')
            return self._not_allowed_view().get(request)


