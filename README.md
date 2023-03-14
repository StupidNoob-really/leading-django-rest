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
AUTH_USER_MODEL = 'api.User'
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

### Создание моделей ```api/models.py```
#### Импорты
```python
from django.db import models
from django.contrib.auth.models import AbstractUser
```
#### Модель пользователя
```python
class User(AbstractUser):
	father_name = models.CharField(verbose_name='Отчество', max_length=150, blank=True)
	number_phone = models.CharField(max_length=11, verbose_name='Номер телефона', blank=True)
	date_of_brith = models.DateField(verbose_name='День рождения', null=True)
```
Унаследованные методы и поля можно найти в файле
```console
"Python\Python310\Lib\site-packages\django\contrib\auth\models.py"
```
#### Модель документов
```python
class Passport(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='passport', verbose_name='Владелец паспорта')
	number = models.CharField(max_length=4, verbose_name='Номер паспорта')
	serial = models.CharField(max_length=6, verbose_name='Серия паспорта')
```
