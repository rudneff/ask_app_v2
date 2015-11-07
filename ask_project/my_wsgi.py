import sys

# start server on another host
# gunicorn -b 127.0.0.1:8081 ask_project.my_wsgi


def app_2(environ, start_response):
    status = "200 OK"
    response_body = "request: {} params: {}".format(environ['REQUEST_METHOD'], environ['QUERY_STRING'])
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    # console print
    # curl --request POST "http://127.0.0.1:8000" - request
    sys.stdout.write('\n\nrequest:\n\n{}\n\n'.format(response_body))
    return ['Hello World!\n', response_body]

application = app_2


# nginx path - /usr/local/etc/nginx/
