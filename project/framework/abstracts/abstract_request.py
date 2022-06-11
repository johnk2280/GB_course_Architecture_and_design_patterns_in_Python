import json
from abc import ABC


class AbstractRequest(ABC):

    environ: dict
    path: str
    method: str
    headers: dict
    query_params: dict

    def _get_headers(self, environ: dict) -> dict:
        headers = {}
        for key, value in environ.items():
            if key.startswith('HTTP_'):
                headers[key[5:].lower()] = value

        return headers

    def _get_query_params(self, environ: dict) -> dict:
        query_params = {}
        try:
            qs = map(
                lambda x: x.split('='),
                environ.get('QUERY_STRING').split('&'),
            )
            for param in qs:
                if query_params.get(param[0]):
                    query_params[param[0]].append(param[-1])
                else:
                    query_params[param[0]] = [param[-1]]
        except (AttributeError, KeyError, TypeError):
            pass

        return {'method': self.method, 'data': query_params}

    def _get_body(self, environ: dict) -> dict:
        body = {}
        body_str = environ['wsgi.input'].read().decode('utf-8')
        return {'method': self.method, 'data': body_str}
