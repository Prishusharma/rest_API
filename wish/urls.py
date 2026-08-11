from django.urls import path

from .views import TeacherListCreateView 

urlpatterns =[
    path("teacher/", TeacherListCreateView.as_view(), name="teachers-list"),
]