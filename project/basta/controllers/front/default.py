from . import Front
from basta.utils.urls import redirect


class RedirectWithoutSlash(Front):
    def process_request(self):
        if self.request.path[-1] != '/':
            return redirect(self.request.path + '/')
