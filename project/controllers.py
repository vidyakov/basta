from basta.controllers.page import Page
from basta.utils.requests import get_post_data
from basta.utils.urls import redirect


class PageWithCommonContextData(Page):
    def get_context_data(self) -> dict:
        menu = [
                {'name': 'index page', 'link': '/'},
                {'name': 'contact page', 'link': '/contact/'},
            ]
        return {'menu': menu}


class IndexPage(PageWithCommonContextData):
    template_name = 'index.html'


class ContactPage(PageWithCommonContextData):
    template_name = 'contact.html'

    def post(self):
        print(get_post_data(self.request))
        return redirect('/')


ROUTES = {
    '/': IndexPage(),
    '/contact/': ContactPage()
}
