from rest_framework import serializers
from courses.models import Courses


class CourseSerialiser(serializers.ModelSerializer):
    """
    serialize user data
    """
    class Meta:
        """
        __summary__
        """
        model = Courses
        fields = '__all__'
