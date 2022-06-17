from framework.abstracts.abstract_model import Model


class User(Model):
    pass


class Course(Model):
    pass


class UserCategory(Model):
    pass


class CourseCategory(Model):
    pass


MODEL_MAPPER = {
    'user': User,
    'course': Course,
    'user_category': UserCategory,
    'course_category': CourseCategory,
}

