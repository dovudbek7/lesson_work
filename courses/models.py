from django.db import models


class Instructor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    speciality = models.TextField()

    def __str__(self):
        return self.name


class Courses(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    starting_date = models.DateField()
    ending_date = models.DateField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)


class Lessons(models.Model):
    lesson_title = models.CharField(max_length=255)
    content = models.TextField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
