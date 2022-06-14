from framework.views import AboutView
from framework.views import ContactView
from framework.views import CourseView
from framework.views import CourseListView
from framework.views import CourseCategoryListView
from framework.views import CreateCourseView
from framework.views import CreateCourseCategoryView
from framework.views import CreateUserCategoryView
from framework.views import CreateUserView
from framework.views import IndexView
from framework.views import UserView
from framework.views import UserCategoryView
from framework.views import UserCategoryListView
from framework.views import UserListView


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
    '/create_user': CreateUserView,
    '/create_user_category': CreateUserCategoryView,
    '/create_course': CreateCourseView,
    '/create_course_category': CreateCourseCategoryView,

}
