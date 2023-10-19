from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('courses/', views.get_courses),
    path('courses/<int:id>/', views.get_specific_course),
    path('courses/<int:course_id>/lessons/', views.get_lessons),
    path('lessons/<int:id>/', views.get_specific_lesson),
    path('instructor/courses/add', views.add_course),
    path('instructor/courses/update/', views.update_course),
    path('instructor/lessons/add/', views.add_lesson),
    path('instructor/lessons/update/', views.update_lesson),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)