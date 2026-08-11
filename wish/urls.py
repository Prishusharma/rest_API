from django.urls import path

from .views import teacherAPIView

urlpatterns =[
    path("teacher/", teacherAPIView.as_view(), name="teachers-list"),
]