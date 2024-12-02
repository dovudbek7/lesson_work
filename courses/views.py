from rest_framework import viewsets
from .serializers import InstructorSerializer, LessonSerializer, CourseSerializer
from .models import Instructor, Courses, Lessons


class InstructorModelViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


class CourseModelViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer


class LessonModelViewSet(viewsets.ModelViewSet):
    queryset = Lessons.objects.all()
    serializer_class = LessonSerializer
