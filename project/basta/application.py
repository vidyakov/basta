from .controllers import code_404, redirect_without_slash


class Basta:
    def __init__(self, routes: dict, fronts: list = []):
        self.routes = routes
        self.fronts = fronts

    def _get_controller(self, request):
        path = request.get('PATH_INFO')

        if path[-1] != '/':
            return redirect_without_slash
        if controller := self.routes.get(path):
            return controller
        return code_404

    def _get_response(self) -> list:
        response = []
        for front in self.fronts:
            front(response)
        return response

    def __call__(self, request: dict, start_response):
        controller = self._get_controller(request)
        status_code, response_headers, body = controller(request)
        response_headers.extend(self._get_response())
        start_response(status_code, response_headers)
        return body,
