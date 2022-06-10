from pathlib import Path

from jinja2 import Template

from settings import PATH_TO_TEMPLATES


def render(template_name: str, **kwargs):
    with open(PATH_TO_TEMPLATES.joinpath(template_name), encoding='utf-8') as f_obj:
        template = Template(f_obj.read())

    return template.render(**kwargs)


class PageNotFound404:
    """Default 404 view"""

    def __call__(self, *args, **kwargs):
        return '404 Page Not Found', render('404.html')


if __name__ == '__main__':
    print(render('index.html'))
