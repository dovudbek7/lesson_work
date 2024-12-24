from rest_framework import status
from django.urls import reverse
from ..models import Instructor

from rest_framework.test import APITestCase


class InstructorAPITest(APITestCase):
    def setUp(self):
        self.instructor = Instructor.objects.create(
            name='John Doe',
            email='test@gmail.com',
            speciality='Backend developer'
        )
        self.list_url = reverse('instructor-list')
        self.detail_url = reverse('instructor-detail', args=[self.instructor.id])

    def test_get_instructor_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_instructor(self):
        data = {
            'name': 'Jane Doe',
            'email': 'jane.doe@gmail.com',
            'speciality': 'Frontend developer'
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Instructor.objects.count(), 2)
