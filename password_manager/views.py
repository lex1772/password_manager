from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from password_manager.models import Data
from password_manager.serializers import DataSerializer
from password_manager.services import encrypt, decrypt


class PasswordRetrieveAPI(APIView):
    """
    Представление для работы с менеджером паролей
    """
    serializer_class = DataSerializer
    queryset = Data.objects.all()

    def get(self, request, service_name):
        """Получение пароля по названию сервиса
         и расшифровка пароля для пользователя"""
        try:
            data = Data.objects.get(service_name=service_name)
        except Exception:
            return Response(data='Нет такого сервиса')
        data.password = decrypt(data.password)
        serializer = DataSerializer(data)
        return JsonResponse(serializer.data)

    def post(self, request, service_name, *args, **kwargs):
        """Создание или редактирование пароля
         по названию сервиса с шифрованием пароля в базу"""
        req = {}
        try:
            req['password'] = request.data['password']
        except KeyError:
            return Response(data='Не заполнен пароль')
        data, created = Data.objects.get_or_create(service_name=service_name)
        data.password = str(encrypt(request.data['password']))
        data.save()
        return JsonResponse(req)


class PasswordListView(generics.ListAPIView):
    """
        Представление для получения списка подходящих паролей через поиск
        """
    serializer_class = DataSerializer

    def get_queryset(self):
        filterurl = self.request.query_params.get('service_name', None)

        if filterurl is not None:
            data_list = Data.objects.filter(service_name__icontains=filterurl)
            password_list = []
            for data in data_list:
                data.password = decrypt(data.password)
                password_list.append(data)
            return password_list
