from .controllers.page import PageNotFound
from .controllers.front import RedirectWithoutSlash
from .http import Request


DEFAULT_FRONTS = [RedirectWithoutSlash()]


class Basta:
    def __init__(self, routes=None, fronts=None):
        self.routes = routes if routes else {}
        self.fronts = fronts + DEFAULT_FRONTS if fronts else DEFAULT_FRONTS

    def _process_request(self, request):
        for front in self.fronts:
            if response := front(request=request):
                return response

    def _get_controller(self, request: Request):
        return self.routes.get(request.path, PageNotFound())

    def _process_response(self, response):
        for front in self.fronts:
            front(response=response)

    def __call__(self, env: dict, start_response):
        request = Request(env)
        response = self._process_request(request)

        if not response:
            controller = self._get_controller(request)
            response = controller(request)
            self._process_response(response)

        start_response(response.status, response.headers)
        return response.body
