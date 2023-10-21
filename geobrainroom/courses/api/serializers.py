from rest_framework import serializers
from courses.models import Courses, Lessons, Progress


class CourseSerialiser(serializers.ModelSerializer):
    """
    serialize course data
    """
    class Meta:
        """
        __summary__
        """
        model = Courses
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    """
    lessons db_table serializer
    """
    class Meta:
        """
        __summary__
        """
        model = Lessons
        fields = '__all__'


class ProgressSerializer(serializers.ModelSerializer):
    """
    Progress db_table serializer
    """
    class Meta:
        """
        __summary__
        """
        model = Progress
        fields = '__all__'