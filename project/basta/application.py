from .controllers import code_404


class Basta:
    headers = [('Content-Type', 'text/html')]

    def __init__(self, routes: dict):
        self.routes = routes

    def get_path(self, env) -> str:
        return env.get('PATH_INFO')

    def get_controller(self, path):
        if controller := self.routes.get(path):
            return controller
        return code_404

    def __call__(self, env: dict, start_response):
        path = self.get_path(env)
        controller = self.get_controller(path)
        code, body = controller()
        start_response(code, self.headers)
        return body
