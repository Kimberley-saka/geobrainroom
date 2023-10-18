"""
views
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from courses.models import Courses
from .serializers import CourseSerialiser



@api_view(['GET'])
def get_courses(request):
    """
    get list of all available courses
    """
    courses = Courses.objects.all()
    serialized = CourseSerialiser(courses, many=True)
    return Response(serialized.data)