"""
"""
from django.db import models
from users.models import Users


class Courses(models.Model):
    """
    __summary__
    """
    course_name = models.CharField(max_length=250, unique=True)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, unique=True)


    class Meta:
        db_table = 'courses'


class Lessons(models.Model):
    """
    __summary__
    """
    course = models.ForeignKey(
        Courses,
        on_delete=models.CASCADE,
        blank=False
    )
    lesson_name = models.CharField(max_length=250)
    files = models.FileField(upload_to='documents/')
    description = models.TextField(max_length=1000, null=True)

 
    class Meta:
        db_table = 'lessons'


class Enroll(models.Model):
    """
    __summary__
    """
    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        blank=False
    )
    course = models.ForeignKey(
        Courses,
        on_delete=models.CASCADE,
        blank=False
    )
    enrolled_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'enroll'
