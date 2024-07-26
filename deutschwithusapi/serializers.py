from rest_framework import serializers
from .models import Course , Resume, Counselling ,User

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        
class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'

class CounsellingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counselling
        fields = '__all__'
        

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['full_name', 'password']

    def create(self, validated_data):
        user = User.objects.User(
            full_name=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            date_of_birth=validated_data['date_of_birth'],
        )
        return user