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
```console
pip install djoser
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
        'rest_framework.authtoken', 
        'api.apps.ApiConfig',
        'djoser', 
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
          'rest_framework.authentication.TokenAuthentication',
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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    father_name = models.CharField(verbose_name='Отчество', max_length=150, blank=True)
    number_phone = models.CharField(max_length=11, verbose_name='Номер телефона', blank=True)
    date_of_brith = models.DateField(verbose_name='День рождения', null=True)
    passport = models.OneToOneField('Passport', on_delete=models.SET_NULL, related_name='user_passport', verbose_name='Паспорт', null=True)
```
Унаследованные методы и поля можно найти в файле
```console
"Python\Python310\Lib\site-packages\django\contrib\auth\models.py"
```
#### Модель документов
```python
class Passport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.CharField(max_length=4, verbose_name='Номер паспорта')
    serial = models.CharField(max_length=6, verbose_name='Серия паспорта')

    def __str__(self):
        return f'{self.number} {self.serial}'
```
### Отправка ответа ```api/views.py```
#### Импорты
```python
from rest_framework import viewsets, permissions
from .serializers import FullUserSerializer, BasicUserSerializer, PassportSerializer
from .models import User, Passport
```
#### Ответ на запрос '/user'
```python
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAdminUser | permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_staff:
                return FullUserSerializer
        return BasicUserSerializer
```
#### Ответ на запрос '/passport'
```python
class PassportViewSet(viewsets.ModelViewSet):
    queryset = Passport.objects.all()
    serializer_class = PassportSerializer
    permission_classes = [permissions.IsAdminUser]
```

### Создание серилайзера ```api\serializer.py```
#### Импорты
```python
from rest_framework import serializers
from .models import User, Passport
```
#### Сериалайзеры для модели User
```python
class BasicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'last_name', 'first_name', 'father_name']
```

```python
class FullUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = []
```

#### Серилайзер для модели Passport
```python
class PassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passport
        exclude = []
```

### Создание маршрутов ```api\urls.py```
#### Импорты
```python
from django.urls import path, include
from . import views
from rest_framework import routers
```
#### Маршруты rest_framework
```python
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='User')
router.register(r'passport', views.UserViewSet, basename='Passport')
```
#### Маршруты django
```python
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', include('djoser.urls')),
    re_path(r'^api-token-auth', include('djoser.urls.authtoken'))
]
```
