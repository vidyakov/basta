from jinja2 import Environment, FileSystemLoader

from basta.config import TEMPLATES_PATH


def render(template_name, **kwargs):
    template = Environment(loader=FileSystemLoader(TEMPLATES_PATH)).get_template(template_name)
    return template.render(**kwargs)
