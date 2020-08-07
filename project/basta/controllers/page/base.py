from basta.http import Response, Request
from basta.utils.templates import render


class Page:
    template_name = None
    status_code = 200
    headers = {}

    @property
    def template(self):
        return render(self.template_name, **self.get_context_data())

    def get_context_data(self) -> dict:
        return {}

    def get_response(self) -> Response:
        return Response(self.template, self.status_code, self.headers)

    def __call__(self, request: Request) -> Response:
        self.request = request

        if self.request.method == 'GET' and hasattr(self, 'get'):
            return self.get()
        if self.request.method == 'POST' and hasattr(self, 'post'):
            return self.post()

        return self.get_response()
