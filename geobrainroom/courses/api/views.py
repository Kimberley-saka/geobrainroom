"""
views
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from courses.models import Courses, Lessons
from .serializers import CourseSerialiser, LessonSerializer



@api_view(['GET'])
def get_courses(request):
    """
    get list of all available courses
    """
    courses = Courses.objects.all()
    if not courses:
        return Response('No courses found',status.HTTP_404_NOT_FOUND)
    serialized = CourseSerialiser(courses, many=True)
    return Response(serialized.data)

@api_view(['GET'])
def get_specific_course(request, id):
    """
    get list of all available courses
    """
    if id is None or not isinstance(id, int):
        return Response('Invalid or missing course id', status=status.HTTP_400_BAD_REQUEST)
    
    course = Courses.objects.filter(id=id).first()

    if course is None:
        return Response('Course not found', status=status.HTTP_404_NOT_FOUND)
    
    serializer = CourseSerialiser(course)
    return Response(serializer.data)


@api_view(['GET'])
def get_lessons(request, course_id):
    """
    Gets a list of lessons in a course
    """
    if course_id is None or not isinstance(course_id, int):
        return Response('Invalid or missing course id', status=status.HTTP_400_BAD_REQUEST)
    
    lessons = Lessons.objects.filter(course_id=course_id)

    if not lessons:
        return Response('Lessons not found', status=status.HTTP_404_NOT_FOUND)

    serializer = LessonSerializer(lessons, many=True)
    return Response(serializer.data)
