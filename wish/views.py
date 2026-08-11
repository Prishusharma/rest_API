from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import teacher
from .serializers import teacherSerializer

class teacherAPIView(APIView):
    def get(self, request):
        teachers = teacher.objects.all()
        serializer = teacherSerializer(teachers, many=True)
        return Response(serializer.data)

