from pprint import pprint


def wsgi_application(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)
    return [(x + '\n').encode('utf8') for x in environ['QUERY_STRING'].split('&')]
