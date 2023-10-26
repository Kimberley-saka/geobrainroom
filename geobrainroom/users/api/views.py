"""
user api
"""
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
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


@api_view(['POST'])
def login(request):
    """
    Login a user
    """
    email = request.data.get('email')
    password = request.data.get('password')

    user = Users.objects.filter(email=email).first()
    if not user:
        return Response( {'detail: User not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if not user.check_password(password): # Password doesnt match
        return Response({'detail: incorrect password'})
    
    authenticated_user = authenticate(request, email=user.email,
                                      password=password)
    
    if authenticated_user:
        login(request, authenticated_user)
        token_serializer = MyTokenObtainPairSerializer(data={'username': user.username})
        token_serializer.is_valid(raise_exception=True)

        token = token_serializer.validated_data['access']
        response = Response('detail: Successfuly logged in')

        response.set_cookie('jwt_token', token)

        return response
    else:
        return Response({'detail: Authentication failed'})

@api_view(['DELETE'])
@staff_member_required
def delete_user(request, id):
    """
    """
    user = Users.objects.get(id=id)
    if not user:
        return Response({'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

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
                            
