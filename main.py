from framework.wsgi import Framework
from framework.urls import url_mapper


app = Framework(url_mapper)
