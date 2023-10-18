from rest_framework import serializers

from password_manager.models import Data


# Сериализатор для данных
class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('password', 'service_name',)
