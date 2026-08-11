from django.contrib import admin
from .models import Course, teacher

@admin.register(teacher)
class teacherAdmin(admin.ModelAdmin):
    list_display=[field.name for field in teacher._meta.fields]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=[field.name for field in Course._meta.fields]
