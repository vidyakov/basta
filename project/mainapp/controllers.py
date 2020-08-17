from basta import App
from basta.controllers.page import Page
from basta.utils.log import Logger, debug
from basta.utils.requests import get_post_data
from basta.utils.urls import redirect

from .models import Category, Course


categories = [Category(name) for name in ('python', 'html', 'css', 'js')]

names = ['Easy Python', 'Hard js', 'Working with html and css']
prices = [500, 1000, 1500]
descs = ['Desc desc desc', 'Desc desc desc', 'Desc desc desc']

courses = [Course(*params) for params in zip(names, prices, descs)]


logger = Logger('mainapp', 'logs')


main_app = App()


class PageWithCommonContextData(Page):
    def get_context_data(self) -> dict:
        menu = (
                {'name': 'index page', 'link': '/'},
                {'name': 'contact page', 'link': '/contact/'},
                {'name': 'admin panel', 'link': '/admin/'}
        )
        return {'menu': menu}


@main_app.route('')
class IndexPage(PageWithCommonContextData):
    template_name = 'index.html'

    @logger.deco('debug')
    def get_context_data(self) -> dict:
        general_data = super().get_context_data()
        return {**general_data, 'courses': courses, 'categories': categories}


@main_app.route('/contact')
class ContactPage(PageWithCommonContextData):
    template_name = 'contact.html'

    @debug
    def post(self):
        print(get_post_data(self.request))
        return redirect('/')


