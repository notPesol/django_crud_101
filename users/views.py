from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .service import create_user, update_user, search_users, delete_user, get_user_by_id

# Create your views here.

@csrf_exempt
def index(request) -> JsonResponse:
    # if method === POST
    # Create user
    if request.method == 'POST':
        return create_user(request.body)
    
    # if method === POST
    # Create user
    elif request.method == 'PUT':
        return update_user(request.body)
        
    # search user
    else:
        return search_users(request.GET)

@csrf_exempt
def get_by_id(request, id):    
    # if Method === DELETE 
    # Delete user
    if request.method == 'DELETE':
       return delete_user(id)
    else:
        return get_user_by_id(id)

    