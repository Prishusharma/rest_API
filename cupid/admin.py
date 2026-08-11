from django.contrib import admin
from .models import Course, Students

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display=[field.name for field in Students._meta.fields]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=[field.name for field in Course._meta.fields]
