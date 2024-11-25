import requests
import json

data_to_send = {
    'name': 'Johan',
    'price': 200.0,
    'image': r'C:\Users\Viktor\Desktop\rest\media\Ad parrot.png'
}

def send_dataJson_to_django(url, payload):
    
    file_to_send = open(r'C:\Users\Viktor\Desktop\rest\media\Ad parrot.png', 'rb')
    files = {'image': file_to_send}
    request = requests.post(url, data_to_send, files=files)
    file_to_send.close()
    response = request
    
    
    print(type(response.content))
    

send_dataJson_to_django('http://127.0.0.1:8000/api/products/', data_to_send)