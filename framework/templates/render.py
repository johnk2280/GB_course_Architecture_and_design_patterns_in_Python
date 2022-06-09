from jinja2 import Template


def render(template_name: str, **kwargs):
    with open(template_name, encoding='utf-8') as f_obj:
        template = Template(f_obj.read())

    return template.render(**kwargs)


# print(render('index.html', nickname='Johnk', status='learning'))

