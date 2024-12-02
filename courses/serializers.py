from rest_framework import serializers
from .models import Instructor, Courses, Lessons
from django.core.exceptions import ValidationError


class InstructorSerializer(serializers.ModelSerializer):
    def validate_email(self, value):
        if "@" not in value:
            raise ValidationError("Invalid email format")
        return value

    class Meta:
        model = Instructor
        fields = ['id', 'name', 'email', 'speciality']


class CourseSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data['starting_date'] > data['ending_date']:
            raise ValidationError("Start date cannot be later than end date")
        return data

    class Meta:
        model = Courses
        fields = ['id', 'title', 'body', 'starting_date', 'ending_date', 'instructor']


class LessonSerializer(serializers.ModelSerializer):
    def validate_order(self, value):
        if value <= 0:
            raise ValidationError("Order must be a positive integer")
        return value

    class Meta:
        model = Lessons
        fields = ['id', 'lesson_title', 'content', 'course', 'order']
