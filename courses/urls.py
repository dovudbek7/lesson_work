from django.urls import path, include
from rest_framework import routers
from courses.views import InstructorModelViewSet, CourseModelViewSet, LessonModelViewSet

router = routers.DefaultRouter()
router.register(r'instructors', InstructorModelViewSet)
router.register(r'courses', CourseModelViewSet)
router.register(r'lessons', LessonModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
