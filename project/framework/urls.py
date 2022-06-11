from framework.views import AboutView
from framework.views import ContactView
from framework.views import IndexView

# urlpatterns = [
#     Url('/', IndexView),
#     Url('/about', AboutView),
#     Url('/contacts', ContactView),
# ]


url_mapper = {
    '/': IndexView,
    '/about': AboutView,
    '/contacts': ContactView,
}
