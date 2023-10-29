"""
views
"""
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from courses.models import (Courses, Lessons, Progress, Enroll)
from users.models import Users
from .serializers import (CourseSerialiser, LessonSerializer,
                          ProgressSerializer, EnrollSerializer)



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
def course_lessons(request, course_id):
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


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def remove_course(request):
    """
    delete a course
    """
    course_name = request.data.get('course_name')

    course = Courses.objects.filter(course_name=course_name).first()

    if course is None:
        return Response({'detail: Course not found or doesnt exist'},
                        status=status.HTTP_404_NOT_FOUND)
    
    course.delete()
    return Response({'detail: Course deleted'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdminUser])
def update_course(request, id):
    """
    Update data
    """
    course = Courses.objects.filter(id=id).first()
    
    if course is None:
        return Response({'error': 'Course does not exist'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = CourseSerialiser(course, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def remove_course(request):
    """
    delete a course
    """
    course_name = request.data.get('course_name')

    course = Courses.objects.filter(course_name=course_name).first()

    if course is None:
        return Response({'detail: Course not found or doesnt exist'},
                        status=status.HTTP_404_NOT_FOUND)
    
    course.delete()
    return Response({'detail: Course deleted'}, status=status.HTTP_204_NO_CONTENT)


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


@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdminUser])
def update_lesson(request, id):
    """
    Update data
    """
    lesson = Lessons.objects.get(id=id)

    if lesson is None:
        return Response({'error': 'lesson doesnt exist'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = LessonSerializer(lesson, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def remove_lesson(request, id):
    """
    delete a course
    """
    
    lesson = Lessons.objects.filter(id=id).first()

    if lesson is None:
        return Response({'detail: Lesson not found or doesnt exist'},
                        status=status.HTTP_404_NOT_FOUND)
    
    lesson.delete()
    return Response({'detail: Losson deleted'}, status=status.HTTP_204_NO_CONTENT)

# Track the porgress of a user

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_progress(request):
    """
    add progress
    """
    user = request.data.get('user_id')
    lesson = request.data.get('lesson_id')

    if Progress.objects.filter(user=user, lesson=lesson).exists():
        return Response({'Lesson already completed'})
    
    progress = {
        "user": user,
        "lesson": lesson 
    }

    serializer = ProgressSerializer(data=progress)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        # Return the serialized data as a JSON response
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def lesson_progress(request, user_id, lesson_id):
    """Retrieve the user and lesson instances progress"""
    progress = Progress.objects.filter(user=user_id, lesson=lesson_id).first()
    if not progress:
        return Response({'Progress not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProgressSerializer(progress)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_completed_lessons(request, user_id):
    """
    get the lessons completed give user_id
    """
    completed_lessons = Lessons.objects.filter(user=user_id)
    if completed_lessons is None:
        return Response({'detail: No completed lesson for this user'}, 
                        status=status.HTTP_404_NOT_FOUND)
    lesson_serializer = LessonSerializer(completed_lessons)
    return Response(lesson_serializer.data)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def enroll_in_course(request):
    """
    enroll
    """
    
    user_id = request.data.get('user_id')
    course_id = request.data.get('course_id')
    
    if Enroll.objects.filter(user_id=user_id, course_id=course_id).exists():
        return Response({'detail: user already enrolled in course'})
    
    serializer = EnrollSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({'detail: sucessfully enrolled'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_course_name_enrolled(request, user_id):
    """
    retrieve a course a user is enrolled in given user_id
    """
    enroll = Enroll.objects.get(user_id=user_id)
    if enroll is None:
        return Response({'detail: Not found'}, status=status.HTTP_404_NOT_FOUND)
    
    course_name = enroll.course_id.course_name

    return Response(course_name)

