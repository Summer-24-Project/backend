from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def calculate(request):
    a = request.data.get('a')
    b = request.data.get('b')
    result = a + b
    return Response({'result': result})
# Create your views here.
