from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson, Subscription
from users.models import User


class MaterialTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='admin@aky.pro')
        self.course = Course.objects.create(title='Математика', description='Математика', owner=self.user)
        self.lesson = Lesson.objects.create(title='Урок 1!', description='Производная',
                                            url='https://www.youtube.com/watch?v=_yqDP_EtM50&list=PLCRqj4jDCIYkL1lREiEg-APcjYbvfqCdn',
                                            course=self.course,
                                            owner=self.user)
        self.subscription = Subscription.objects.create(course=self.course, user=self.user)

        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("materials:lesson-retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), 'Урок 1!')

    def test_lesson_create(self):
        url = reverse("materials:create-lesson")
        data = {
            "title": "Урок 2!",
            "description": "Первообразная, практика",
            "url": "https://www.youtube.com/watch?v=_yqDP_EtM50&list=PLCRqj4jDCIYkL1lREiEg-APcjYbvfqCdn",
            "course": self.course.pk
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse("materials:lesson-update", args=(self.lesson.pk,))
        data = {
            "title": "Урок 1! Погнали",
            "url": "https://www.youtube.com/watch?v=_yqDP_EtM50&list=PLCRqj4jDCIYkL1lREiEg-APcjYbvfqCdn"
        }
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), 'Урок 1! Погнали')

    def test_lesson_delete(self):
        url = reverse("materials:lesson-delete", args=(self.lesson.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse("materials:lesson-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_subscription(self):
        url = reverse("materials:subscription")
        data = {
            "course": self.course.pk
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
