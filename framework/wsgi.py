from .response import Response
from .request import Request
from .views import View


class Framework:

    def __init__(self, urls):
        self.urls = urls

    def __call__(self, environ, start_response):
        request = Request(environ)
        view = self._get_view(request)
        response = self._get_response(request, view)

        start_response(response.status, list(response.headers.items()))
        return [response.body.encode()]

    def _get_view(self, request: Request):
        path = request.path
        print(1, path)
        for url in self.urls:
            print(2, url.path)
            if url.path == path:
                return url.view

            return

    def _get_response(self, request: Request, view: View):
        if hasattr(view, request.method):
            return getattr(view, request.method)(view, request)

        return Response(status='404 NOT FOUND', body='404.html')
