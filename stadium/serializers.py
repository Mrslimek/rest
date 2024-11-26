from rest_framework import serializers
from .models import PeopleCategory, ServiceCategory, Service, Subservice
# from rest_framework.validators import UniqueValidator

# СЕРИАЛИЗАТОРЫ ДЛЯ ПОЛУЧЕНИЯ И СОХРАНЕНИЯ JSON-ОВ МОДЕЛЕЙ СО СВЯЗЬЮ FOREIGNKEY

class ServiceCategorySerializer(serializers.Serializer):
    
    """
    Возвращает словарь с полем title модели ServiceCategory
    """
    
    title = serializers.CharField()
    
class ServiceSerializerExcludeForeignKey(serializers.Serializer):
    
    """
    Возвращает словарь с полями модели Service,
    за исключением поля со связью
    """
    
    title = serializers.CharField()
    image = serializers.ImageField()
    description = serializers.CharField()
    best = serializers.BooleanField()
    
# class SubserviceSerializer(serializers.Serializer):
    
#     """
#     Возвращает словарь с полями модели Subservice
#     """
    
#     title = serializers.CharField()
#     unit = serializers.CharField()
#     price = serializers.DecimalField(max_digits=20, decimal_places=2)

    
class SubserviceSerializerExcludeForeignKey(serializers.Serializer):
    
    """
    Возвращает словарь с полями модели Subservice,
    за исключением поля со связью
    """
    
    title = serializers.CharField()
    unit = serializers.CharField()
    price = serializers.DecimalField(max_digits=20, decimal_places=2)
    

class ServiceSerializerIncludeSubserviceSet(serializers.Serializer):

    """
    Возвращает словарь с полями модели Service,
    Включая поля модели Subservice
    """
    
    title = serializers.CharField()
    description = serializers.CharField()
    best = serializers.BooleanField()
    subservice_set = SubserviceSerializerExcludeForeignKey(many=True)

class ServiceSerializer(serializers.Serializer):
    
    """
    Возвращает словарь с полями модели Service
    """
    
    title = serializers.CharField()
    description = serializers.CharField()
    best = serializers.BooleanField()
    service_category = serializers.CharField()
    
    def create(self, validated_data):
        
        service_category, created = ServiceCategory.objects.get_or_create(title=validated_data['service_category'])
        validated_data['service_category'] = service_category
        service, created = Service.objects.get_or_create(**validated_data)
        return service
        
class ServiceCategoryModelSerializer(serializers.ModelSerializer):
    
    """
    Возвращает словарь с полем title модели ServiceCategory
    """
    
    services = ServiceSerializer(many=True)
    
    class Meta:
        model = ServiceCategory
        fields = ['title', 'services']

class ForeignKeyServicesSerializer(serializers.Serializer):
    
    """
    Возвращает словарь с информацией для Артема
    """
    
    title = serializers.CharField()
    service_set = ServiceSerializerIncludeSubserviceSet(many=True)

        
class ServiceSerializerForSasha(serializers.Serializer):
    
    title = serializers.CharField()
    description = serializers.CharField()
    best = serializers.BooleanField()
    
    def create(self, validated_data):
        return Service.objects.create(**validated_data)
    
class ServiceCategorySerializerForSasha(serializers.Serializer):

    title = serializers.CharField()
    service_set = ServiceSerializerForSasha(many=True)

    def create(self, validated_data):
        
        service_category_instance, service_category_created = ServiceCategory.objects.get_or_create(title=validated_data.get('title'))
        for data in validated_data.get('service_set'):    
            service_instance, service_created = Service.objects.get_or_create(**data,service_category=service_category_instance)
        
        return service_category_instance
    
# СЕРИАЛИЗАТОРЫ ДЛЯ ПОЛУЧЕНИЯ И СОХРАНЕНИЯ JSON-ОВ МОДЕЛЕЙ СО СВЯЗЬЮ ManyToMany

class PeopleSerializer(serializers.Serializer):
    
    '''
    Возвращает словарь с данными о модели PeopleCategory - т.е. name и last_name
    '''
    
    name = serializers.CharField()
    last_name = serializers.CharField()

# class CategoryUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ServiceCategory
#         fields = '__all__'

class CategoryUserSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)

# class ManyToManySerializer(serializers.ModelSerializer):
#     category_user = CategoryUserSerializer(many=True)
    
#     class Meta:
#         model = PeopleCategory
#         fields = ['name', 'last_name', 'category_user']

#     def create(self, validated_data):
#             category_user_data = validated_data.pop('category_user')
#             people_category, created = PeopleCategory.objects.get_or_create(**validated_data)
#             for service_category_data in category_user_data:
#                 service_category, created = ServiceCategory.objects.get_or_create(**service_category_data)
#                 people_category.category_user.add(service_category)
            
class ManyToManySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    category_user = CategoryUserSerializer(many=True)
    
    def create(self, validated_data):
        category_user_data = validated_data.pop('category_user')
        print(type(validated_data))
        people_category, created = PeopleCategory.objects.get_or_create(**validated_data)
        for service_category_data in category_user_data:
            service_category, created = ServiceCategory.objects.get_or_create(**service_category_data)
            people_category.category_user.add(service_category)
        return people_category
