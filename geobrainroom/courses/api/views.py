"""
views
"""
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from courses.models import Courses, Lessons, Progress
from users.models import Users
from .serializers import CourseSerialiser, LessonSerializer, ProgressSerializer



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
@permission_classes([IsAuthenticated, IsAdminUser])
def add_course(request):
    """
    Create new course
    """
    course_name = request.data.get('course_name')

    if Courses.objects.filter(course_name=course_name).exists():
        return Response({'Course already exists'})

    new_course = CourseSerialiser(data=request.data)
    if new_course.is_valid():
        new_course.save()
    
    else:
        raise ValidationError('Invalid data entered')
    
    return Response(new_course.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdminUser])
def update_course(request, course_id):
    """
    Update data
    """
    course_id = request.data.get('course_id')

    try:
        course = Courses.objects.get(course_id=id)
    except Courses.DoesNotExist:
        return Response({'error': 'Course does not exist'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = CourseSerialiser(course, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def add_lesson(request):
    """
    Create a new lesson
    """
    lesson_name = request.data.get('lesson_name')

    if Lessons.objects.filter(lesson_name=lesson_name).exists():
        return Response({'Lesson already exists'})
    
    new_lesson = LessonSerializer(data=request.data)

    if new_lesson.is_valid():
        new_lesson.save()

    else:
        raise ValidationError('Invalid data entered')
    
    return Response(new_lesson.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdminUser])
def update_lesson(request):
    """
    Update data
    """
    lesson_name = request.data.get('lesson_name')

    try:
        lesson = Lessons.objects.get(lesson_name=lesson_name)
    except Lessons.DoesNotExist:
        return Response({'error': 'lesson doesnt exist'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = LessonSerializer(lesson, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Track the porgress of a user
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def lesson_progress(request, user_id, lesson_id):
    """Retrieve the user and lesson instances"""
    user = get_object_or_404(Users, pk=user_id)
    lesson = get_object_or_404(Lessons, pk=lesson_id)

    if request.method == 'GET':
        progress = Progress.objects.filter(user=user, lesson=lesson).first()
        if not progress:
            return Response({'Progress not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProgressSerializer(progress)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Create or update progress
        progress = Progress.objects.create(user=user, lesson=lesson)

        progress.completed = True
        progress.save()

        serializer = ProgressSerializer(progress)

        # Return the serialized data as a JSON response
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def enroll_user(request):
    """
    Get the courses a user is enrolled in
    """
    pass