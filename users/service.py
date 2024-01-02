from django.http import JsonResponse
from django.db.utils import IntegrityError
from django.utils import timezone

import json

from .models import User

from .dto import ResponseDTO
from .utils import to_dict_user

def create_user(request_body):
    responseDTO = ResponseDTO()

    raw_data = request_body.decode('utf-8')
    
    # Parse JSON data
    json_data = json.loads(raw_data)

    # Retrieve specific values from JSON data
    username = json_data.get('username', None)
    password = json_data.get('password', None)
    
    errors = []
    if not username:
        errors.append('username is required.')
        
    if not password:
        errors.append('password is required.')
    
    if errors:
        responseDTO.message = ", ".join(errors)
        return JsonResponse(responseDTO.to_dict(), safe=False)
    
    try:
        user = User(username=username,password=password)
        user.save()
        responseDTO.data = to_dict_user(user)
    except IntegrityError:
        responseDTO.message = 'username already exists.'
        
    return JsonResponse(responseDTO.to_dict(), safe=False)

def update_user(request_body):
    responseDTO = ResponseDTO()

    # Access raw request body
    raw_data = request_body.decode('utf-8')

    # Parse JSON data
    json_data = json.loads(raw_data)

    # Retrieve specific values from JSON data
    id = json_data.get('id', None)
    if not id:
        responseDTO.message = "id is required."
        return JsonResponse(responseDTO.to_dict(), safe=False)
    
    username = json_data.get('username', None)
    password = json_data.get('password', None)
    
    try:
        user = User.objects.get(pk=id)

        if username:
            user.username = username
        if password:
            user.password = password
            
        user.updated_at = timezone.now()
        user.save()
        responseDTO.data = to_dict_user(user)
    except IntegrityError:
        responseDTO.message = 'username already exists.'
    except User.DoesNotExist:
        responseDTO.message = f'user id = {id} does not exist.'
        
    return JsonResponse(responseDTO.to_dict(), safe=False)

def search_users(request_query):
    ignore_page = request_query.get('ignore_page', False)   
    page = int(request_query.get('page', 1))    
    limit = int(request_query.get('limit', 20))   
    
    if not(ignore_page):
        print(page, limit)
        offset = (page - 1) * limit
        users = User.objects.all()[offset:limit * page]
    else:
        users = User.objects.all()
        
    data = []
    for user in users:
        data.append(to_dict_user(user))
        
    responseDTO = ResponseDTO(data=data)
    
    return JsonResponse(responseDTO.to_dict(), safe=False)

def delete_user(id):
    responseDTO = ResponseDTO()
    status = 204
    try:
        user = User.objects.get(pk = id)
        
        user.delete()
        responseDTO.message = 'deleted'
            
        responseDTO.data = to_dict_user(user)
    except User.DoesNotExist:
        responseDTO.message = 'not found.'
        status = 404
        responseDTO.data = None

    return JsonResponse(responseDTO.to_dict(), safe=False, status=status)

def get_user_by_id(id):
    responseDTO = ResponseDTO()
    status = 200
    try:
        user = User.objects.get(pk = id)
        responseDTO.data = to_dict_user(user)
    except User.DoesNotExist:
        responseDTO.message = 'not found.'
        status = 404
        responseDTO.data = None

    return JsonResponse(responseDTO.to_dict(), safe=False, status=status)