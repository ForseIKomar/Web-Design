from cgi import parse_qs


def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)

    if (environ['REQUEST_METHOD'] == 'POST'):
	query = parse_qs(environ['wsgi.input'].read())
    	printingString = '\n'.join('%s = %s' % (i.decode('utf8'), j[0].decode('utf8')) for i, j in query.items())
    else:
    	printingString = '\n'.join('{ }'.format(i) for i in environ['QUERY_STRING'].split('&'))
    return [('{}\n{}\n'.format(environ['REQUEST_METHOD'], printingString)).encode('utf-8')]

