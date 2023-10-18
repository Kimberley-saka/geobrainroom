from django.urls import path
from . import views


urlpatterns = [
    path('courses/', views.get_courses),
    path('courses/<int:pk>/', views.get_specific_course)
]