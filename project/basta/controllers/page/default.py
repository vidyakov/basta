from . import Page
from basta.http import Response


class PageNotFound(Page):
    def get_response(self):
        template = 'Page not found'
        return Response(template, 404, self.headers)
