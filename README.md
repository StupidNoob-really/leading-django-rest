# Работа с django и rest_framework

## Устновка библиотек
```console
pip install django
```
```console
pip install djangoreactframework
```
```console
pip install psycopg2
```
## Создание проекта
```console
django-admin startproject server
```
## Создание приложения
```console
cd server
python manage.py startapp api
```
## Настройка проекта
### Файл ```server\settings.py```
#### Инцилизация приложений
```python
    INSTALLED_APPS = {
        'rest_framework',
        'api.apps.ApiConfig',
        ...
    }
```
#### Подключение к базе данных
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': database_name,
        'USER': user_name,
        'PASSWORD': user_password,
        'HOST': db_host,
        'PORT': db_port,
    }
}
```
#### Поменять модель пользователя
```python
AUTH_USER_MODEL = 'Apps.User'
```
#### Директория статических файлов
```python
STATIC_URL = 'static/'
```
#### Тип поля индефикатора
```python
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```
>or
```python
DEFAULT_AUTO_FIELD = 'django.db.models.UUIDField'
```
#### Кофнигурация rest_framework
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}
```
### Файл ```server\urls.py```
#### Импорты
```python
from django.contrib import admin
from django.urls import path, include
```
#### Указания маршрутов
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
```
