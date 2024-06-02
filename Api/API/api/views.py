from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import GreetingSerializer
from .models import Greeting

# Create your views here.


@api_view(['GET'])
def greet(request):
    greeting = Greeting(message="Hello, World!")
    serializer = GreetingSerializer(greeting)
    return Response(serializer.data)