from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class DataTestCase(APITestCase):
    # Тесты для данных пользователя

    def test_without_password(self):
        # Создание сервиса без пароля
        response = self.client.post(reverse('password_manager:password',
                                            kwargs={'service_name': 'vk'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), "Не заполнен пароль")

    def test_post(self):
        # Создание сервиса с паролем
        response = self.client.post(reverse('password_manager:password',
                                            kwargs={'service_name': 'vk'}),
                                    data={'password': '123'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'password': '123'})

    def test_update(self):
        # Обновление пароля
        self.client.post(reverse('password_manager:password',
                                 kwargs={'service_name': 'vk'}),
                         data={'password': '123'})
        response = self.client.post(reverse('password_manager:password',
                                            kwargs={'service_name': 'vk'}),
                                    data={'password': '12345'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'password': '12345'})

    def test_get(self):
        # Получение пароля
        self.client.post(reverse('password_manager:password',
                                 kwargs={'service_name': 'vk'}),
                         data={'password': '12345'})
        response = self.client.get(reverse('password_manager:password',
                                           kwargs={'service_name': 'vk'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {'password': '12345', 'service_name': 'vk'})

    def test_get_search(self):
        # Получение пароля
        self.client.post(reverse('password_manager:password',
                                 kwargs={'service_name': 'vk'}),
                         data={'password': '12345'})
        url = '{url}?{filter}={value}'.format(
            url=reverse('password_manager:password_list'),
            filter='service_name', value='v')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         [{'password': '12345', 'service_name': 'vk'}])
