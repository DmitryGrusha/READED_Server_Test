import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from user.models import User


@csrf_exempt
def registration_request(request):
    if request.method == 'POST':
        # try:
            # return decode(request)
        return JsonResponse({})
        # except json.JSONDecodeError:
        #     return JsonResponse({'type': 'ERROR', 'answer': 'Invalid JSON format.'})
    else:
        return JsonResponse({'type': 'ERROR', 'answer': 'Method not allowed.'})


def decode(request):
    data = json.loads(request.body.decode('utf-8'))
    #
    # # if ['name', 'last_name', 'phone'] in data:
    # if 'name' in data and 'phone' in data:
    #     return save_user(data)
    # else:
    #     return JsonResponse({'type': 'ERROR', 'answer': 'Invalid JSON format or missing fields.'})


def save_user(data):
    name = data['name']
    # last_name = data['last_name']
    # phone = data['phone']
    #
    # if not is_already_exist(phone):
    #     user = User(name=name, phone=phone)
    #     user.save()
    #     return JsonResponse({'type': 'SUCCESS', 'answer': 'User created.'})
    # else:
    #     return JsonResponse({'type': 'ERROR', 'answer': 'User already exist.'})


def is_already_exist(phone):
    return User.objects.filter(phone=phone).exists()
