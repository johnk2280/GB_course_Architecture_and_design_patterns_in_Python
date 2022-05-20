from pprint import pprint
from request import Request


def application(environ: dict, start_response) -> list:
    # print(environ['wsgi.input'].read().decode())
    # pprint(environ)
    request = Request(environ)
    print(request.method)
    print(request.path)
    print(request.headers)
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'Hello world from my first wsgi application!!!']
