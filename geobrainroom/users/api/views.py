"""
user api
"""
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.admin.views.decorators import staff_member_required
from .serializers import UserSerialiser
from users.models import Users


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
        'api/add'
    ]
    return Response(routes)


@api_view(['POST'])
def add_user(request):
    """
    create new user
    """
    user_serializer = UserSerialiser(data=request.data)
    if user_serializer.is_valid(): #check if data passed is valid
        user_serializer.save()

    else:
        error = user_serializer.errors
        return Response(f'Oops and error occured: {error}', status=status.HTTP_400_BAD_REQUEST)
    
    return Response(user_serializer.data)

@api_view(['DELETE'])
@staff_member_required
def delete_user(request,):
    try:
        pk = request.data.get('pk', None)
        if pk is None or not isinstance(pk, int):
            return Response({'Invalid or missing user ID'},
                            status=status.HTTP_400_BAD_REQUEST)
        user = Users.objects.get(pk=pk) # Search for user in db
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
    