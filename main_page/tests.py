from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User

from .models import FieldModel

class FieldModelTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.field_model = FieldModel.objects.create(support="Support", helped="Helped", partner="Partner")

    def test_get_field_model_list(self):
        """
        Тестирование получения списка моделей FieldModel.
        """
        url = reverse('fieldmodel-list')

        # Имитация аутентификации
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_field_model_detail(self):
        """
        Тестирование получения деталей модели FieldModel.
        """
        url = reverse('fieldmodel-detail', args=[self.field_model.id])

        # Имитация аутентификации
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['support'], self.field_model.support)

    def test_create_field_model(self):
        """
        Тестирование создания модели FieldModel.
        """
        url = reverse('fieldmodel-list')
        data = {'support': 'New Support', 'helped': 'New Helped', 'partner': 'New Partner'}

        # Имитация аутентификации
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(FieldModel.objects.count(), 2)
        self.assertEqual(FieldModel.objects.last().support, 'New Support')

    def test_update_field_model(self):
        """
        Тестирование обновления модели FieldModel.
        """
        url = reverse('fieldmodel-detail', args=[self.field_model.id])
        data = {'support': 'Updated Support', 'helped': 'Updated Helped', 'partner': 'Updated Partner'}

        # Имитация аутентификации
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user)

        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(FieldModel.objects.get(id=self.field_model.id).support, 'Updated Support')

    def test_delete_field_model(self):
        """
        Тестирование удаления модели FieldModel.
        """
        url = reverse('fieldmodel-detail', args=[self.field_model.id])

        # Имитация аутентификации
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user)

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(FieldModel.objects.count(), 0)
