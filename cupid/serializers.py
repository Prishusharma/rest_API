from rest_framework import serializers

from .models import Course, Student


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    # Read-only nested representation
    # Used when returning student data
    course = CourseSerializer(read_only=True)

    # Write-only field
    # Used when receiving student data
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), source="course", write_only=True
    )

    class Meta:
        model = Student
        fields = (
            "id",
            "name",
            "age",
            "email",
            "course",
            "course_id",
            "is_active",
        )

        # Custom error messages
        extra_kwargs = {  # noqa: RUF012
            "name": {
                "error_messages": {
                    "required": "Student name is required.",
                    "blank": "Student name cannot be empty.",
                }
            },
            "email": {
                "error_messages": {
                    "required": "Email address is required.",
                }
            },
        }

    # Field-level validation
    def validate_age(self, value):

        if value < 18:
            raise serializers.ValidationError("Student must be at least 18 years old.")

        if value > 100:
            raise serializers.ValidationError("Please enter a valid age.")

        return value

    # Object-level validation
    def validate(self, data):

        if data.get("name", "").lower() == "admin":
            raise serializers.ValidationError(
                {"name": "Student name 'admin' is not allowed."}
            )

        return data