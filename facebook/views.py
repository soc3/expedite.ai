from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from pprint import pprint
import json

# Create your views here.

def hello(_):
    return HttpResponse("hello")


@csrf_exempt
def live_api_callback(request):
    if request.method == 'GET':
        key = request.GET['hub.challenge']
        return HttpResponse(key)

    data = json.loads(request.body)
    pprint(data)
    return HttpResponse('gosudocode')
