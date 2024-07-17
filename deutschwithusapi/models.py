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
    name = models.CharField(max_length= 100)
    major = models.CharField(max_length=100)
    date = models.DateTimeField()
    type = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class counselling(models.Model) :
    topic = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    def __str__(self):
        return self.topic