class App:
    def __init__(self, fronts=None, url_prefix: str = ''):
        self._routes = {}
        self._fronts = fronts or []
        self.url_prefix = url_prefix

    @property
    def routes(self):
        return {f'{self.url_prefix}{key}/': value for key, value in self._routes.items()}

    @property
    def fronts(self):
        return self._fronts.copy()

    def route(self, path: str):
        """ Route class based page controllers """
        def wrapper(cls):
            self._routes[path] = cls()
            return cls
        return wrapper

    def route_func(self, path: str):
        """ Route function based page controllers """
        def deco(func):
            def wrapper(*args, **kwargs):
                self._routes[path] = func
                return func(*args, **kwargs)
            return wrapper
        return deco
