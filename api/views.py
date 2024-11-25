from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from django.http import FileResponse, HttpResponse

# Create your views here.

@api_view(['GET', 'POST'])
def get_products(request):
    
    products = Product.objects.all()
    
    if request.method == 'POST':
        
        message = {'message':'succes'}
        
        data = request.data
        # print(type(request.data))
        print(request.data)
        
        serializer = ProductSerializer(data = data)
        if serializer.is_valid():
            
            print(serializer.validated_data)
            # print(serializer.data)
            
            product_object = Product(
                name = request.data.get('name'),
                price = request.data.get('price'),
                image = request.data.get('image')
            )
        
            product_object.save()
            
            uploaded_file = request.FILES['image']
            print(uploaded_file)
            
            response_data = {
                'file_name': uploaded_file.name,
                'name': request.data.get('name'),
                'price': request.data.get('price'),
                'message': 'Файл успешно загружен!'
            }
            return FileResponse(response_data)
            
        else:
            print(serializer.errors)
                
    return FileResponse({'message':'Well done'})
