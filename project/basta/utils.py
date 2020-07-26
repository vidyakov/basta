from jinja2 import Environment, FileSystemLoader

from .config import TEMPLATES_PATH, ENCODING


def get_path(request: dict) -> str:
    return request.get('PATH_INFO')


def get_request_method(request: dict) -> str:
    return request.get('REQUEST_METHOD')


def render(template_name, **kwargs):
    template = Environment(loader=FileSystemLoader(TEMPLATES_PATH)).get_template(template_name)
    return template.render(**kwargs).encode(ENCODING)


def _make_dict_from_query(query: str) -> dict:
    return dict(map(lambda elem: elem.split('='), query.split('&')))


def get_data_from_query_string(request: dict) -> dict or None:
    if data := request.get('QUERY_STRING'):
        return _make_dict_from_query(data)


def get_post_data(request: dict) -> dict or None:
    if data := request['wsgi.input'].read().decode(ENCODING):
        return _make_dict_from_query(data)
