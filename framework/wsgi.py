from pprint import pprint


def application(environ, start_response) -> list:
    start_response('200 OK', [('Content-Type', 'text/html')])
    print(environ['wsgi.input'].read().decode())
    pprint(environ)
    return [b'Hello world from my first wsgi application!!!']
