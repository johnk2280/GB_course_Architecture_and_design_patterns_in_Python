from framework.wsgi import Framework
from framework.url import Url
from framework.view import View


class MyFirstView(View):

    def get(self, request, *args, **kwargs):
        return 'Я ГЕТ запрос'

    def post(self, request, *args, **kwargs):
        return 'Я ПОСТ запрос'


urls = [
    Url('/', MyFirstView),
]

app = Framework(urls)
