from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class teacher(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="teachers"
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
            return self.name