from django.db import models

# Create your models here.

class ServiceCategory(models.Model):
    
    """
    Определяет какие категории есть у услуг
    Является первичной моделью по отношению к модели Service
    """
    
    title = models.CharField(max_length=255, verbose_name='Название категории', unique=True)
    
    class Meta:
        verbose_name = 'Категория услуги'
        verbose_name_plural = 'Категории услуг'
    
    def __str__(self):
        return self.title


class PeopleCategory(models.Model):
    
    """
    Модель описывает отношения людей к категориям
    """
    
    name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    category_user = models.ManyToManyField('serviceCategory')
    
    class Meta:
        verbose_name = 'Пользователь категории'
        verbose_name_plural = 'Пользователи категорий'
        
    def __str__(self):
        return self.name
    
    
class Service(models.Model):
    
    """
    Определяет данные, которые хранятся в бд об услугах
    Является вторичной моделью по отношению к модели ServiceCategory
    и первичной по отношению к модели Subservice
    """
    
    title = models.CharField(max_length=255, verbose_name='Название услуги', unique=True)
    image = models.ImageField(upload_to='./stadium', verbose_name='Картинка', null=True, blank=True)
    description = models.TextField(verbose_name='Описание')
    best = models.BooleanField(default=False, verbose_name='Продвигаемая')
    service_category = models.ForeignKey('ServiceCategory', on_delete=models.CASCADE, verbose_name='Категория')
    
    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'
    
    def __str__(self):
        return self.title


class Subservice(models.Model):
    
    """
    Определяет данные, которые хранятся в бд о подуслугах
    Является вторичной моделью по отношению к модели Service
    Подуслуга услуги, которая описана в классе Service выше
    """
    
    title = models.CharField(max_length=255, verbose_name='Название подуслуги', unique=True)
    unit = models.CharField(max_length=255, verbose_name='Единицы измерения')
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Цена')
    type_of_service = models.ForeignKey('Service', on_delete=models.CASCADE, verbose_name='Услуга')
    
    class Meta:
        verbose_name = 'Подуслуги'
        verbose_name_plural = 'Подуслуги'
    
    def __str__(self):
        return f'{self.title} --- {self.unit} --- {self.price}'