"""
urls`
"""
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView)
from . import views
from .views import MyTokenObtainPairView


urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', views.logout, name='logout'),
    path('create/', views.create_user),
    path('profile/', views.get_user_profile),
    path('profile/reset/password/', views.reset_password),
    path('', views.get_routes)
    
]
