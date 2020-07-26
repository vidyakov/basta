from basta.controllers import redirect
from basta.utils import render, get_post_data, get_request_method


def index_page(request) -> (str, list, bytes):
    template_name = 'index.html'
    return '200 OK', [], render(template_name, title='Index page')


def contact_page(request) -> (str, list, bytes):
    if get_request_method(request) == 'GET':
        return '200 OK', [], render('contact.html', title='Contact page')

    data = get_post_data(request)
    print(f'Name: {data.get("name")}\nEmail: {data.get("email")}')
    return redirect('/')
