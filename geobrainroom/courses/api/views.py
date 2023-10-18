from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_routes(request):
    routes = [
        'api/get_course'
    ]
    return Response(routes)


@api_view(['GET'])
def hello(request):
    return Response({'Hello world'})