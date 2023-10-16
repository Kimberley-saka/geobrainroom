"""
"""
from django.db import models

class Courses(models.Model):
    """
    __summary__
    """
    course_name = models.CharField(max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, unique=True)


    class Meta:
        db_table = 'courses'


class Lessons(models.Model):
    """
    __summary__
    """
    lesson_name = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)


    class Meta:
        db_table = 'lessons'


class Enrol(models.Model):
    """
    __summary__
    """
    enrolled_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'enrol'
