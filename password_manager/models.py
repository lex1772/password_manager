from django.db import models


class Data(models.Model):
    # Модель для данных пользователя
    service_name = models.CharField(max_length=255,
                                    unique=True,
                                    verbose_name='название сервиса')
    password = models.CharField(max_length=255, verbose_name='пароль')

    def __str__(self):
        return f'{self.service_name}'

    class Meta:
        verbose_name = 'данные'
        verbose_name_plural = 'данные'
