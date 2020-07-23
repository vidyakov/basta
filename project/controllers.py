from os.path import abspath

from basta.utils import render


def index_page() -> (str, list):
    template_path = abspath('templates/index.html')
    return '200 OK', render(template_path, title='Index page')


def contact_page() -> (str, list):
    template_path = abspath('templates/index.html')
    return '200 OK', render(template_path, title='Contact page')
