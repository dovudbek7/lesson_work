from django.test import TestCase
from ..models import Instructor


class InstructorModelTest(TestCase):
    def setUp(self):
        """
        Har bir test methodidan oldin ishga tushadi
        """
        self.instructor = Instructor.objects.create(
            name='John Doe',
            email='test@gmail.com',
            speciality='Backend developer'
        )

    def test_instructor_creation(self):
        """
        Instructor obyektining to'g'ri yaratilganini tekshirish
        """
        instructor = Instructor.objects.get(name='John Doe')
        self.assertEqual(instructor.email, 'test@gmail.com')
        self.assertEqual(instructor.speciality, 'Backend developer')

    def test_instructor_str_method(self):
        """
        Instructor modelining __str__ metodi to'g'ri ishlashini tekshirish
        """
        self.assertEqual(str(self.instructor), 'John Doe')
