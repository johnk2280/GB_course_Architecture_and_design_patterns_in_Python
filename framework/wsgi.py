from .request import Request
from .view import View


class Framework:

    def __init__(self, urls):
        self.urls = urls

    def __call__(self, environ, start_response):
        request = Request(environ)
        view = self._get_view(request)
        response = self._get_response(request, view)

        start_response(response.st, [('Content-Type', 'text/html')])
        return [b'Hello world from my first wsgi application!!!']

    def _get_view(self, request: Request):
        path = request.path
        for url in self.urls:
            if url.path == path:
                return url.view

            return

    def _get_response(self, request: Request, view: View):
        if hasattr(view, request.method):
            return getattr(view, request.method)(view, request)

        return 'Метод не поддерживается.'
