class Request:

    def __init__(self, environ: dict):
        self.environ = environ
        self.method = environ.get('REQUEST_METHOD')
        self.path = environ.get('PATH_INFO')
        self.query_string = self._get_query_string(environ)
        self.headers = self._get_headers(environ)

    def _get_headers(self, environ: dict) -> dict:
        headers = {}
        for key, value in environ.items():
            if key.startswith('HTTP_'):
                headers[key[5:].lower()] = value

        return headers

    def _get_query_string(self, environ: dict) -> dict:
        return {}

