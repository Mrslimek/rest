from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PeopleCategory, ServiceCategory, Service, Subservice
from .serializers import (
                        ServiceCategorySerializer, ServiceSerializer,
                        ServiceSerializerExcludeForeignKey, SubserviceSerializerExcludeForeignKey,
                        ForeignKeyServicesSerializer, ServiceCategoryModelSerializer,
                        ServiceCategorySerializerForSasha, ServiceSerializerForSasha,
                        PeopleSerializer, ManyToManySerializer)
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth.models import User

# Create your views here.

# ВЬЮШКИ ДЛЯ ПОЛУЧЕНИЯ И СОХРАНЕНИЯ JSON-ОВ МОДЕЛЕЙ СО СВЯЗЬЮ FOREIGNKEY
class ServiceView(APIView):
    def get(self, request):
        
        service = Service.objects.all()
        serializer = ServiceSerializer(service, many=True)
        
        return Response(serializer.data)
    
    def post(self, request):
        
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'success'})
        
        return Response(serializer.errors)
    
@api_view(['GET', 'POST'])
def create_service_from_list(request):

    serializer = ServiceSerializer(data=request.data, many=True)
    
    if serializer.is_valid():    
        serializer.save()
        return Response({'message':'success'})
    
    return Response(serializer.errors)


class SubserviceView(APIView):
    
    def get(self, request):
        subservices = Subservice.objects.all()
        
        serializer = SubserviceSerializerExcludeForeignKey(subservices, many=True)
        
        return Response(serializer.data)

@api_view(['GET'])
def get_full_data(request):
    
    data = ServiceCategory.objects.all()
    print(data)
    serializer = ForeignKeyServicesSerializer(data, many=True)
    
    return Response(serializer.data)
    
class ServiceCategoryView(APIView):
    def get(self, request):
        
        service_category = ServiceCategory.objects.all()
        serializer = ServiceCategorySerializer(service_category, many=True)
        
        return Response(serializer.data)
    
    def post(self, request):
        
            serializer = ServiceCategorySerializerForSasha(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'success'})
            
            return Response(serializer.errors)

@api_view(['POST'])
def create_service_category_from_list(request):
        
        serializer = ServiceCategorySerializerForSasha(data=request.data, many=True)
        
        if serializer.is_valid():
            
            service_category_list = []
            service_list = []
            
            for data in serializer.validated_data:
                category = ServiceCategory.objects.filter(title=data['title']).first()
                # print(category)
                if not category:
                    category = ServiceCategory(title=data['title'])
                    service_category_list.append(category)
                    
                for service_data in data['service_set']:
                    service = Service.objects.filter(title=service_data['title']).first()
                    # print(service)
                    if not service:
                        service = Service(
                            title=service_data['title'],
                            description=service_data['description'],
                            best=service_data['best'],
                            service_category=category
                        )
                        service_list.append(service)
                        
            ServiceCategory.objects.bulk_create(service_category_list)
            Service.objects.bulk_create(service_list)
            return Response({'message': 'success'})
        
        return Response(serializer.errors)
    
# class CreateServiceCategoryFromList(APIView):

#     def post(self, request):
        
#         serializer = ServiceCategorySerializerForSasha(data=request.data, many=True)
        
#         if serializer.is_valid():
            
#             service_data_list = []
#             service_category_list = []
            
#             for data in serializer.validated_data:
#                 service_data_list.append(data.pop('service_set'))
#                 service_category_list, created = ServiceCategory.objects.get_or_create(**data)
            
#             # print(service_category_list)
            
#             for service_data in service_data_list:
#                 for data in service_data:
#                     Service.objects.get_or_create(**data, service_category=service_category_list)
            
#             return Response({'message': 'success'})
        
#         return Response(serializer.errors)

# class CreateServiceCategoryFromList(generics.CreateAPIView):

#     '''
#     Делает все то же самое, что и класс выше, но тут используется наследование от generics.CreateAPIView.
#     По сути то же самое, но логика, описаная в методе post класса Homework написана в методе create у
#     сериализатора ServiceCategoryForSasha
#     '''

#     queryset = ServiceCategory.objects.all()
#     serializer_class = ServiceCategorySerializerForSasha

# ВЬЮШКИ ДЛЯ ПОЛУЧЕНИЯ И СОХРАНЕНИЯ JSON-ОВ МОДЕЛЕЙ СО СВЯЗЬЮ ManyToMany

class PeopleView(APIView):
    
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):

        people = PeopleCategory.objects.all()
        serializer = PeopleSerializer(people, many=True)        

        return Response(serializer.data)

class PeopleCategoryView(APIView):
    def get(self, request):
    
        people_category = PeopleCategory.objects.all()
        serializer = ManyToManySerializer(people_category, many=True)
        
        return Response(serializer.data)

    def post(self, request):
    
        serializer = ManyToManySerializer(data=request.data)
        
        if serializer.is_valid():        
            serializer.save()
            return Response({'message': 'success'})
        
        return Response(serializer.errors)

@api_view(['POST'])
def create_people_category_from_list(request):
    
    serializer = ManyToManySerializer(data=request.data, many=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'success'})
    
    return Response(serializer.errors)

class RegisterView(APIView):
    def post(self, request):
        
        user = User.objects.create_user(username=request.data['username'], password=request.data['password'])
        token = Token.objects.create(user=user)
    
        return Response({'message': token.key})


# class LoginView(APIView):
#     def post(self, request):
        

        #c32cb85e796f828a086076a7f4206bf54b111ee9

        #eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.dyt0CoTl4WoVjAHI9Q_CwSKhl6d_9rhM3NrXuJttkao