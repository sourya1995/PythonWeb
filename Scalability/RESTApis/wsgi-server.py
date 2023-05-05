from wsgiref.simple_server import make_server

def application(environ, start_response):
    body = '\n'.join(['%s:%s' % (key, value) for key, value in sorted(environ.items())])
    start_response("200 OK", [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(body)))

    ])

    return [body.encode()]

httpd = make_server('localhost', 10000, application)
httpd.handle_request()