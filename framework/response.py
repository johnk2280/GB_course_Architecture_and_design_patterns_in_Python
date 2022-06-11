from framework.abstracts.abstract_response import AbstractResponse
from framework.render import render_view


class Response(AbstractResponse):
    def __init__(
            self,
            status: str = '200 OK',
            headers: dict = None,
            body: str = None,
    ):
        self.status = status
        self.headers = self._get_headers(headers)
        self.body = render_view(body)

    def _get_headers(self, user_headers: dict) -> dict:
        headers = {
            'Content-Type': 'text/html',
        }
        if user_headers:
            headers.update(user_headers)

        return headers
