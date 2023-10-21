"""
"""
from django.db import models
from users.models import Users


class Courses(models.Model):
    """
    __summary__
    """
    course_name = models.CharField(max_length=250, unique=True)
    description = models.TextField(max_length=1000, null=True)
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
    description = models.TextField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

 
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


class Progress(models.Model):
    """
    For progress tracking
    """
    lesson = models.ForeignKey(
        Lessons,
        on_delete=models.CASCADE,
        blank=False
    )

    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        blank=False
    )

    completed = models.BooleanField(null=True)
    completed_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        """
        """

        db_table = "progress"
