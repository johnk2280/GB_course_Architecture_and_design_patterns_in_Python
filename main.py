from framework.wsgi import Framework
from framework.url import Url
from framework.view import View
from framework.response import Response

from framework.templates import render


class MyFirstView(View):

    def get(self, request, *args, **kwargs) -> Response:
        return Response(body=render('index.html'))

    def post(self, request, *args, **kwargs) -> Response:
        return Response(status='201 CREATED', body='POST SUCCESS')


urls = [
    Url('/', MyFirstView),
]

app = Framework(urls)
