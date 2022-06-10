from framework.abstracts.abstract_view import View
from framework.render import render
from framework.response import Response


class IndexView(View):
    def get(self, request, *args, **kwargs) -> Response:
        return Response(body='index.html')


class AboutView(View):
    def get(self, request, *args, **kwargs) -> Response:
        return Response(body='about.html')


class ContactView(View):
    def get(self, request, *args, **kwargs) -> Response:
        return Response(body='contacts.html')

