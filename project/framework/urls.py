from framework.views import AboutView
from framework.views import CourseView
from framework.views import CourseListView
from framework.views import CourseCategoryListView
from framework.views import UserView
from framework.views import UserCategoryView
from framework.views import UserCategoryListView
from framework.views import UserListView
from framework.views import ContactView
from framework.views import IndexView


url_mapper = {
    '/': IndexView,
    '/about': AboutView,
    '/contacts': ContactView,
    '/users': UserListView,
    '/courses': CourseListView,
    '/user_categories': UserCategoryListView,
    '/course_categories': CourseCategoryListView,
    '/get_user': UserView,
    '/get_user_category': UserCategoryView,
    '/get_course': CourseView,
    '/get_course_category': CourseView,

}
