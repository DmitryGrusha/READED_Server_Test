import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user.models import User


@csrf_exempt
def get_user(request):
    return JsonResponse({'type': 'ERROR', 'answer': 'Method not allowed.'})
