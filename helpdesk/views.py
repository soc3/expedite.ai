from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


from helpdesk.models import Issue, Reply, Order, ISSUE_STATUSES
# Create your views here.


def get_issues_by_category(request):
    return render(request, 'index.html')
    try:
        issues = Issue.objects.filter(category=request.GET['q'])
    except KeyError:
        return JsonResponse({'message': 'query value not provided'}, status=400)
    else:
        return JsonResponse([each.to_json() for each in issues], safe=False)


def get_issues_by_status(request):
    try:
        issues = Issue.objects.filter(status=request.GET['q'])
    except KeyError:
        return JsonResponse({'message': 'query value not provided'}, status=400)
    else:
        return JsonResponse([each.to_json() for each in issues], safe=False)


def resolve_issue(request):
    try:
        comment_id = request.GET['id']
        issue = Issue.objects.get(comment_id=comment_id)
        issue.status = ISSUE_STATUSES['closed']
        issue.save()
    except KeyError:
        return JsonResponse({'message': 'comment id not provided'}, status=400)
    else:
        return JsonResponse({'message': 'resolved'}, status=200)


def archive_issue(request):
    try:
        comment_id = request.GET['id']
        issue = Issue.objects.get(comment_id=comment_id)
        issue.status = ISSUE_STATUSES['archived']
        issue.save()
    except KeyError:
        return JsonResponse({'message': 'comment id not provided'}, status=400)
    else:
        return JsonResponse({'message': 'archived'}, status=200)


def reopen_issue(request):
    try:
        comment_id = request.GET['id']
        issue = Issue.objects.get(comment_id=comment_id)
        issue.status = ISSUE_STATUSES['open']
        issue.save()
    except KeyError:
        return JsonResponse({'message': 'comment id not provided'}, status=400)
    else:
        return JsonResponse({'message': 'reopened'}, status=200)


def get_chat(request):
    try:
        replies = Reply.objects.filter(issue__comment_id=request.GET['q'])
        issue = Issue.objects.get()
        messages = [each.to_json() for each in replies]
        messages.insert(0, issue.to_json())
    except KeyError:
        return JsonResponse({'message': 'issue id not provided'}, status=200)
    else:
        return JsonResponse(messages, safe=False)
