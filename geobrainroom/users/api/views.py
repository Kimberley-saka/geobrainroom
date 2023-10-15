"""
user api
"""
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerialiser


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """custom claim jwt"""
    @classmethod
    def get_token(cls, user):
        """
        __summary__
        """
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    """
    serialize
    """
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def get_routes(request):
    """
    retrieve all the routes in this api
    """
    routes = [
        'api/token',
        'api/token/refresh',
        'api/create_user'
    ]
    return Response(routes)


@api_view(['POST'])
def add_user(request):
    """
    create new user
    """
    user_serializer = UserSerialiser(data=request.data)
    if user_serializer.is_valid():
        user_serializer.save()

    else:
        error = user_serializer.errors
        return Response(f'Oops and error occured: {error}', status=status.HTTP_400_BAD_REQUEST)
    
    return Response(user_serializer.data)
