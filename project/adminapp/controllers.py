from basta.controllers.page import Page
from basta.utils.requests import get_post_data
from basta.utils.urls import redirect

from mainapp.models import Course, Category
from mainapp.controllers import courses, categories


class PageWithCommonContextData(Page):
    def get_context_data(self) -> dict:
        menu = (
            {'name': 'index page', 'link': '/'},
            {'name': 'contact page', 'link': '/contact/'},
            {'name': 'admin panel', 'link': '/admin/'}
        )
        commands = (
            {'name': 'Create new course', 'link': '/admin/new_course/'},
            {'name': 'Create new category', 'link': '/admin/new_category/'}
        )
        return {'commands': commands, 'menu': menu}


class AdminPanel(PageWithCommonContextData):
    template_name = 'admin_panel.html'


class CreateCourse(PageWithCommonContextData):
    template_name = 'create_course.html'

    def post(self):
        form_data = get_post_data(self.request)
        new_course = Course(
            name=form_data.get('name'),
            price=form_data.get('price'),
            desc=form_data.get('desc')
        )
        courses.append(new_course)
        return redirect('/admin/')


class CreateCategory(PageWithCommonContextData):
    template_name = 'create_category.html'

    def post(self):
        form_data = get_post_data(self.request)
        new_category = Category(
            name=form_data.get('name')
        )
        categories.append(new_category)
        return redirect('/admin/')
