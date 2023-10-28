"""
user api
"""
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
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
        'api/add',
        'api/<int:pk>/delete',
        '/api/courses',
        'courses/<int:pk>/lessons/',
    ]
    return Response(routes)


@api_view(['POST'])
def create_user(request):
    """
    create new user
    """
    email = request.data.get('email')
   
    if Users.objects.filter(email=email).exists():
        return Response({'detail: User already exists'}, status=status.HTTP_409_CONFLICT)
    
    new_user = UserSerialiser(data=request.data) 
    new_user.is_valid(raise_exception=True) #check if data passed is valid
    new_user.save()
    return Response(new_user.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    """
    get an authenticated user
    """
    authentication_classes = [JWTAuthentication]
    user = request.user
    serializer = UserSerialiser(user, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
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
                            
