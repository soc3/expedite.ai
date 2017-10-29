from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


from helpdesk.models import Issue, Reply, Order, ISSUE_STATUSES
# Create your views here.


def get_issues(request):
    issues = Issue.objects.filter()
    return JsonResponse([each.to_json() for each in issues], safe=False)


def get_chat(request, issue_id):
    replies = Reply.objects.filter(issue__comment_id= issue_id)
    return JsonResponse([each.to_json() for each in replies])
