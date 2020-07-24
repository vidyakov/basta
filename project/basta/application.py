from .controllers import code_404


class Basta:
    headers = [('Content-Type', 'text/html')]

    def __init__(self, routes: dict, fronts: list):
        self.routes = routes
        self.fronts = fronts

    def get_path(self, env) -> str:
        path = env.get('PATH_INFO')
        path += '/' if path[-1] != '/' else ''
        return path

    def get_controller(self, path):
        if controller := self.routes.get(path):
            return controller
        return code_404

    def set_fronts(self) -> dict:
        request = {}
        for front in self.fronts:
            front(request)
        return request

    def __call__(self, env: dict, start_response):
        path = self.get_path(env)
        controller = self.get_controller(path)
        request = self.set_fronts()
        code, body = controller(request)
        start_response(code, self.headers)
        return body,
