from django.urls import path

from .views import StudentsAPIView

urlpatterns =[
    path("students/", StudentsAPIView.as_view(), name="students-list"),
]