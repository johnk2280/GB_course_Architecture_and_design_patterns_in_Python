from framework.abstracts.url import Url
from framework.views import AboutView
from framework.views import ContactView
from framework.views import IndexView

urlpatterns = [
    Url('/', IndexView),
    Url('/about', AboutView),
    Url('/contacts', ContactView),
]
