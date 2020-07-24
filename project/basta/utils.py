from jinja2 import Environment, FileSystemLoader

from .config import TEMPLATES_PATH


def render(template_name, **kwargs):
    template = Environment(loader=FileSystemLoader(TEMPLATES_PATH)).get_template(template_name)
    return template.render(**kwargs).encode('utf-8')
