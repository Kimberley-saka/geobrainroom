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

    def __str__(self):
        return self.course_name


    class Meta:
        db_table = 'courses'


class Lessons(models.Model):
    """
    __summary__
    """
    course_id = models.ForeignKey(
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
    user_id = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        blank=False
    )
    course_id = models.ForeignKey(
        Courses,
        on_delete=models.CASCADE,
        blank=False
    )
    enrolled =  models.BooleanField(default=True)
    enrolled_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Uername: {self.user_id.username} Course_enrolled: {self.course_id.name}"
        


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
