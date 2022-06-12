from jinja2 import Template
from jinja2 import FileSystemLoader
from jinja2.environment import Environment


from settings import PATH_TO_TEMPLATES


def render_view(template_name: str, **kwargs) -> str:
    file_loader = FileSystemLoader(PATH_TO_TEMPLATES)
    env = Environment(loader=file_loader)
    template = env.get_template(template_name)

    return template.render(**kwargs)


if __name__ == '__main__':
    print(render_view('index.html', data={'name': 'Evgen', 'status': 'ok'}))
