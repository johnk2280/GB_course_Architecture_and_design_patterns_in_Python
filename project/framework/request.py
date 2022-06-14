from framework.abstracts.abstract_request import AbstractRequest


class GetRequest(AbstractRequest):

    def __init__(self, environ):
        self.environ = environ
        self.method = environ.get('REQUEST_METHOD').lower()
        self.path = environ.get('PATH_INFO')
        self.headers = self._get_headers(environ)
        self.query_params = self._get_query_params(environ)


class PostRequest(AbstractRequest):

    def __init__(self, environ):
        self.environ = environ
        self.method = environ.get('REQUEST_METHOD').lower()
        self.path = environ.get('PATH_INFO')
        self.headers = self._get_headers(environ)
        self.body = self._get_body(environ)
        
        
METHOD_MAPPER = {
    'get': GetRequest,
    'post': PostRequest,
}


class Request:

    def __new__(cls, environ: dict):
        method = environ.get('REQUEST_METHOD').lower()
        try:
            return METHOD_MAPPER[method](environ)
        except KeyError:
            return
            
        

