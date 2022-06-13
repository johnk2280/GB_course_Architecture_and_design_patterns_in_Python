from abc import ABC
import json
from urllib.parse import parse_qs


class AbstractRequest(ABC):

    environ: dict
    path: str
    method: str
    headers: dict
    query_params: dict

    def __init__(self, environ: dict):
        self.environ = environ
        self.method = environ.get('REQUEST_METHOD').lower()
        self.path = environ.get('PATH_INFO')
        self.headers = self._get_headers(environ)
        self.query_params = self._get_query_params(environ)

    def _get_headers(self, environ: dict) -> dict:
        headers = {}
        for key, value in environ.items():
            if key.startswith('HTTP_'):
                headers[key[5:].lower()] = value

        return headers

    def _get_query_params(self, environ: dict) -> dict:
        if self.method == 'get':
            query_params = parse_qs(environ.get('QUERY_STRING'))
        else:
            query_params = parse_qs(environ['wsgi.input'].read().decode())

        return {'method': self.method, 'data': query_params}
