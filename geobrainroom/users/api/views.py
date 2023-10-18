"""
user api
"""
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
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
        'api/add',
        'api/<int:pk>/delete',
        '/api/courses',
    ]
    return Response(routes)


@api_view(['POST'])
def add_user(request):
    """
    create new user
    """
    password = request.data.get('password', None)
    new_user = UserSerialiser(data=request.data) # Serialize the incoming data
    if new_user.is_valid(): #check if data passed is valid
        new_user.save()

    else:
        error = new_user.errors
        return Response(f'Oops and error occured: {error}', status=status.HTTP_400_BAD_REQUEST)
    
    return Response(new_user.data)

@api_view(['DELETE'])
def delete_user(request, pk):
    try:
        pk = request.data.get('pk', None)
        if pk is None or not isinstance(pk, int):
            return Response({'Invalid or missing user ID'},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            user = User.objects.get(pk=pk) # Search for user in db
    except user.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def update_password(request):
    """
    __summary__
    """
    email = request.data.get('email', None)
    password = request.data.get('password', None)

    if email is None or not isinstance(email, str):
        return Response({'Invalid or missing user email'},
                            status=status.HTTP_400_BAD_REQUEST)
    if password is None or not isinstance(password, str):
        return Response({'Invalid or missing user password'},
                            status=status.HTTP_400_BAD_REQUEST)
