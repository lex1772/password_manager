from django.urls import path

from password_manager.apps import PasswordManagerConfig
from password_manager.views import PasswordRetrieveAPI, PasswordListView

app_name = PasswordManagerConfig.name

# Урлы для паролей
urlpatterns = [
    path(
        "password/<str:service_name>",
        PasswordRetrieveAPI.as_view(),
        name='password'
    ),
    path(
        "password/",
        PasswordListView.as_view(),
        name='password_list'
    )
]
