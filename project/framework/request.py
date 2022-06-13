from framework.abstracts.abstract_request import AbstractRequest


class GetRequest(AbstractRequest):
    pass


class PostRequest(AbstractRequest):
    pass

        
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
            
        

