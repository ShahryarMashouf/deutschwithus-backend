from django.shortcuts import render
from .serializers import CourseSerializer, ResumeSerializer, CounsellingSerializer, UserSerializer
from .models import Course,Resume,Counselling
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import SignupForm
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        
        token['username'] = user.username
       

        return token
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view()
@permission_classes(IsAuthenticated)
def secret(request):
    return Response({"message":"Its secret baby"})

def signUp(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account is created successfully")
            return redirect('home')
        else:
            messages.error(request,"Error")
    else: 
        form = SignupForm()
    return render(request,"registration.html", {'form': form})

def logIn(request):
    return render(request, "login.html")


class SignUpView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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

@api_view(['GET'])
def resume(request):
    items = Resume.objects.all()
    serializer = ResumeSerializer(items, many=True)
    return Response({'Resume':serializer.data})

@api_view(['GET'])
def counselling(request):
    items = Counselling.objects.all()
    serializer = CounsellingSerializer(items, many=True)
    return Response({'Counselling':serializer.data})

@api_view(['GET'])
def courseDetail(request,pk):
    courses = Course.objects.get(id=pk)
    serializer = CourseSerializer(courses, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def resumeDetail(request,pk):
    resumes = Resume.objects.get(id=pk)
    serializer = ResumeSerializer(resumes, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def counsellingDetail(request,pk):
    counsellings = Counselling.objects.get(id=pk)
    serializer = CounsellingSerializer(counsellings, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def courseDelete(request,pk):
    courses = Course.objects.get(id=pk)
    courses.delete()
    return Response('Course succesfully deleted!')

@api_view(['DELETE'])
def resumeDelete(request,pk):
    resumes = Resume.objects.get(id=pk)
    resumes.delete()
    return Response('Resume succesfully deleted!')

@api_view(['DELETE'])
def counsellingDelete(request,pk):
    counsellings = Counselling.objects.get(id=pk)
    counsellings.delete()
    return Response('Object succesfully deleted!')

