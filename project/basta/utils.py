from jinja2 import Template, Environment, BaseLoader


def render(template_name, **kwargs):
    with open(template_name, 'r', encoding='utf-8') as file:
        template = Template(file.read())

    template = Environment(loader=BaseLoader()).from_string(template)
    return template.render(**kwargs).encode('utf-8')
