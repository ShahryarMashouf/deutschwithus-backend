from django.urls import path
from . import views
from . views import SignUpView , MyTokenObtainPairView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
   
    TokenRefreshView,
)

urlpatterns = [
    path('', views.courses, name="courses-list"),  
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('courses/', views.courses, name="courses-list"),  
    path('course-create/', views.courseCreate, name= "courseCreate"),
    path('course-detail/<str:pk>/', views.courseDetail, name="course-detail"),
    path('course-delete/<str:pk>/', views.courseDelete, name="course-delete"),
    path('resume/', views.resume, name= "resume"),
    path('resume-detail/<str:pk>/', views.resumeDetail, name="resume-detail"),
    path('resume-delete/<str:pk>/', views.resumeDelete, name="resume-delete"),
    path('counselling/', views.counselling, name= "counselling"),
    path('counselling-detail/<str:pk>/', views.counsellingDetail, name="counselling-detail"),
    path('counselling-delete/<str:pk>/', views.counsellingDelete, name="counselling-delete"),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('registration/',views.signUp, name="signUp"),
    path('secret/', views.secret),
    path('api-token-auth/', obtain_auth_token),
    path('login/',views.logIn, name="login"),
 
]
