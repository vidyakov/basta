import time

from termcolor import cprint

from basta.controllers.page import PageNotFound
from basta.controllers.front import RedirectWithoutSlash
from basta.http import Request
from basta.utils.meta import Singleton
from .abc import AbstractApplication


DEFAULT_FRONTS = [RedirectWithoutSlash()]


class FakeBasta(AbstractApplication):
    def __call__(self, env: dict, start_response):
        start_response('200 OK', [])
        return b'HELLO FROM FAKE',


class Basta(AbstractApplication, metaclass=Singleton):
    def __init__(self, apps=None):
        self._routes = {}
        self._fronts = DEFAULT_FRONTS
        for app in apps:
            self._routes.update(app.routes)
            self._fronts += app.fronts

    @property
    def routes(self):
        return self._routes.copy()

    def _process_request(self, request):
        for front in self._fronts:
            if response := front(request=request):
                return response

    def _get_controller(self, request: Request):
        return self._routes.get(request.path, PageNotFound())

    def _process_response(self, response):
        for front in self._fronts:
            front(response=response)

    def __call__(self, env: dict, start_response):
        self.request = Request(env)
        self.response = self._process_request(self.request)

        if not self.response:
            controller = self._get_controller(self.request)
            self.response = controller(self.request)
            self._process_response(self.response)

        start_response(self.response.status, self.response.headers)
        return self.response.body


class BastaWithLogger(AbstractApplication, metaclass=Singleton):
    def __init__(self, apps=None):
        self.application = Basta(apps)

    @staticmethod
    def _log_request(env):
        request = Request(env)
        message = f'REQUEST TIME: {time.time()} METHOD: {request.method} QUERY_STRING: {request.query_string}'
        cprint(message, 'red')

    def __call__(self, env: dict, start_response):
        self._log_request(env)
        return self.application(env, start_response)
