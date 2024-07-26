from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    level = models.CharField(max_length=50)
    time = models.TimeField()
    start_date = models.DateField()
    end_date = models.DateField()
    def __str__(self):
        return self.name
    
    
class Resume(models.Model):
    major = models.CharField(max_length=100)
    date = models.DateTimeField()
    type = models.CharField(max_length=100)
    def __str__(self):
        return self.major
    
class Counselling(models.Model) :
    topic = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    def __str__(self):
        return self.topic

class User(models.Model):
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.EmailField()
    date_of_birth = models.DateField()
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.full_name