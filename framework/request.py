class Request:

    def __init__(self, environ: dict):

        self.environ = environ
        self.method = environ.get('REQUEST_METHOD').lower()
        self.path = environ.get('PATH_INFO')
        self.query_string = self._get_query_params(environ)
        self.headers = self._get_headers(environ)

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

        return query_params
