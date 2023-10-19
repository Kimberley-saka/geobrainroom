"""
views
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
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
    get a course
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

@api_view(['GET'])
def get_specific_lesson(request, id):
    """
    Retrieve contents of a lesson
    """
    lesson = Lessons.objects.filter(id=id).first()

    if not lesson:
        return Response('Lesson not found', status.HTTP_404_NOT_FOUND)

    serializer = LessonSerializer(lesson)
    return Response(serializer.data)


@api_view(['POST'])
#@staff_member_required
def add_course(request):
    """
    Create new course
    """
    new_course = CourseSerialiser(data=request.data)
    if new_course.is_valid():
        new_course.save()
    
    else:
        raise ValidationError
    return Response(new_course.data)

@api_view(['PUT'])
#@staff_member_required
def update_course(request, id):
    """
    Update
    """
    course_to_update = get_object_or_404(Courses, id=id)
    serializer = CourseSerialiser(course_to_update, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_lesson(request):
    """
    Create a new lesson
    """
    try:
        new_lesson = LessonSerializer(data=request.data)
        if new_lesson.is_valid():
            new_lesson.save()

    except Exception as e:
        print(e)

    return Response(new_lesson.data)
