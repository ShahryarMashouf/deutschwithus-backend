from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.courses, name="courses-list"),  
    path('coursecreate/', views.courseCreate, name= "courseCreate"),
]
