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
    path('courses/update/<int:id>', views.update_course),
    path('courses/delete/', views.remove_course),
    path('lessons/add/', views.add_lesson),
    path('lessons/update/<int:id>', views.update_lesson),
    path('lessons/<int:id>/', views.get_specific_lesson),
    path('user/<int:user_id>/lessons/<lesson_id>/progress', views.lesson_progress),
]
