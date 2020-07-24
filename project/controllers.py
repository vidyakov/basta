from basta.utils import render


def index_page(request) -> (str, list):
    template_name = 'index.html'
    return '200 OK', render(template_name, title='Index page')


def contact_page(request) -> (str, list):
    template_name = 'contact.html'
    return '200 OK', render(template_name, title='Contact page')
