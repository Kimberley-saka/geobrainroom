from rest_framework import serializers
from courses.models import Courses, Lessons, Progress, Enroll


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

    class EnrollSerializer(serializers.ModelSerializer):
        """
        enroll db_table serializer
        """
        class Meta:
            """
            __summary__
            """
            model = Enroll
            fields = '__all__'