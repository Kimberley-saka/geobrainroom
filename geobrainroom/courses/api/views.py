"""
views
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
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

@api_view(['GET'])
def get_specific_course(request, pk):
    """
    get list of all available courses
    """
    if pk is None or not isinstance(pk, int):
        return Response('Invalid or missing course id', status=status.HTTP_400_BAD_REQUEST)
    
    course = Courses.objects.filter(pk=pk).first()

    if course is None:
        return Response('Course not found', status=status.HTTP_404_NOT_FOUND)
    
    serializer = CourseSerialiser(course)
    return Response(serializer.data)

