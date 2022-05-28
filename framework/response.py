class Response:

    def __init__(
            self,
            body: str = None,
            status: str = '200 OK',
            headers: dict = None
    ):
        self.status = status
        self.headers = self._get_headers(headers)
        self.body = body

    def _get_headers(self, user_headers: dict) -> dict:
        headers = {
            'Content-Type': 'text/html',
        }
        if user_headers:
            headers.update(user_headers)

        return headers
