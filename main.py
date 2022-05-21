from framework.wsgi import Framework
from framework.url import Url
from framework.view import View
from framework.response import Response


class MyFirstView(View):

    def get(self, request, *args, **kwargs) -> Response:
        return Response(status=200, body='GET SUCCESS')

    def post(self, request, *args, **kwargs) -> Response:
        return 'Я ПОСТ запрос'


urls = [
    Url('/', MyFirstView),
]

app = Framework(urls)
