from pathlib import Path

from jinja2 import Template

from settings import PATH_TO_TEMPLATES


def render_view(template_name: str, **kwargs) -> str:
    with open(PATH_TO_TEMPLATES.joinpath(template_name), encoding='utf-8') as f_obj:
        template = Template(f_obj.read())

    return template.render(**kwargs)




if __name__ == '__main__':
    print(render_view('index.html'))
