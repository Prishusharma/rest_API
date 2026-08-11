from .models import Course, teacher
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class teacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = teacher
        fields = '__all__'