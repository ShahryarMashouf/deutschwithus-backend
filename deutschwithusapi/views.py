from django.shortcuts import render
from .serializers import CourseSerializer
from .models import Course
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status



@api_view(['GET'])
def courses(request):
    items = Course.objects.all()  
    serializer = CourseSerializer(items, many=True) 
    return Response({'course':serializer.data})

@api_view(['POST'])
def courseCreate(request):
    serializer = CourseSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)