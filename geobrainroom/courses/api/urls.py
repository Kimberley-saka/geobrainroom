"""
URLs
"""
from django.urls import path
from . import views


urlpatterns = [
    path('courses/', views.get_courses),
    path('courses/<int:id>/', views.get_specific_course),
    path('courses/<int:course_id>/lessons/', views.course_lessons),
    path('courses/add/', views.add_course),
    path('courses/update/<int:id>/', views.update_course),
    path('courses/delete/', views.remove_course),
    path('lessons/add/', views.add_lesson),
    path('lessons/update/<int:id>/', views.update_lesson),
    path('lessons/<int:id>/', views.get_specific_lesson),
    path('lessons/delete/<int:id>/', views.remove_lesson),
    path('enroll/', views.enroll_in_course),
    path('enroll/course/<int:user_id>/', views.get_course_name_enrolled),
    path('progress/add/', views.create_progress),
    path('lessons/progress/<int:user_id>/<lesson_id>/', views.lesson_progress),
    path('lessons/progress/<int:user_id>/', views.get_completed_lessons)
]
