from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from facebook.utils import sanitize, comment
from helpdesk.models import Issue, Reply

from pprint import pprint
import json
from datetime import datetime

# Create your views here.

def hello(_):
    return HttpResponse("hello")


@csrf_exempt
def live_api_callback(request):
    if request.method == 'GET':
        key = request.GET['hub.challenge']
        return HttpResponse(key)

    try:
        data = json.loads(request.body)
        print('recieved webhook from facebook')
        newobj = sanitize(data)
        print(newobj)
        if newobj['issue']:
            print('new object')
            i, _ = Issue.objects.get_or_create(comment_id=newobj['comment'])
            i.category = newobj['categories']
            i.from_name = newobj['name']
            i.status = newobj['type']
            i.message = newobj['message']
            i.priority = 1
            i.created_at = datetime.fromtimestamp(newobj['date'])
            i.updated_at = datetime.fromtimestamp(newobj['date'])
            i.save()
            print(i)

        else:
            r = Reply.objects.create(
                comment_id=newobj['id'],
                issue=Issue.objects.get(comment_id=newobj['comment']),
                message=newobj['message'],
                created_at=datetime.fromtimestamp(newobj['date']),
                from_name=newobj['name'],
            )
            r.save()

    except Exception as e:
        print(e)
    return HttpResponse('gosudocode')


@csrf_exempt
def comment_on_fb(request):
    comment_id = request.POST['comment_id']
    message = request.POST['message']
    print(comment_id, message)
    res, ok = comment(message, comment_id)
    print(ok, res)
    return HttpResponse('ok')
