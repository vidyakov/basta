import basta.config


class Request:
    def __init__(self, request: dict):
        self.method = request.get('REQUEST_METHOD')
        self.path = request.get('PATH_INFO')
        self.query_string = request.get('QUERY_STRING')
        self.form = request.get('wsgi.input').read().decode(basta.config.ENCODING)

        self._data = request
