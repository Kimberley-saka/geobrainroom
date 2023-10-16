from django.db import models

class Courses(models.Model):
    """
    __summary__
    """
    course_name = models.CharField(max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, unique=True)


class lessons(models.Model):
    """
    __summary__
    """
    pass


class Enrol(models.Model):
    """
    __summary__
    """
    pass
