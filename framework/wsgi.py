from .response import Response
from .request import Request
from .views import View, PageNotFound404View, MethodNotAllowedView


class Framework:
    urls: dict

    def __init__(self, urls):
        self.urls = urls
        self._not_found_view = PageNotFound404View
        self._not_allowed_view = MethodNotAllowedView

    def __call__(self, environ: dict, start_response: callable):
        print(*environ.items(), sep='\n')
        request = Request(environ)
        view = self._get_view(request)
        response = self._get_response(request, view)
        start_response(response.status, list(response.headers.items()))
        return [response.body.encode()]

    def _get_view(self, request: Request) -> View:
        try:
            return self.urls[request.path]
        except KeyError:
            return self._not_found_view
        except AttributeError:
            return self._not_allowed_view

    def _get_response(self, request: Request, view: View):
        try:
            return getattr(view, request.method)(view, request)
        except AttributeError:
            return Response(status='405 Method Not Allowed', body='405.html')


