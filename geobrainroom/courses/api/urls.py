from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('courses/', views.get_courses),
    path('courses/<int:id>/', views.get_specific_course),
    path('courses/<int:course_id>/lessons/', views.get_lessons),
    path('lessons/<int:id>/', views.get_specific_lesson),
    path('instructor/courses', views.add_course),
    path('instructor/courses/<int:id>/', views.update_course),
    path('instructor/lessons/', views.add_lesson),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)