from django.contrib import admin
from .models import Instructor, Courses, Lessons

admin.site.register(Instructor)
admin.site.register(Courses)
admin.site.register(Lessons)
