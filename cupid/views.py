from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Students
from .serializers import StudentsSerializer

class StudentsAPIView(APIView):
    def get(self, request):
        students = Students.objects.all()
        serializer = StudentsSerializer(students, many=True)
        return Response(serializer.data)

   

# Create your views here.
