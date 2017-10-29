from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


from helpdesk.models import Issue, Reply, Order, ISSUE_STATUSES, ISSUE_CATEGORIES
from facebook.utils import comment
# Create your views here.


def index(request):
    return get_issues_by_category(request)


def get_default_context(request):
    try:
        q = request.GET['q']
    except KeyError:
        q = 'where is my order'

    category_count = {each: Issue.objects.filter(category=each).count()
                        for each in ISSUE_CATEGORIES}
    context = {
        'issue_categories': category_count,
        'active_category': q,
    }
    return context


def get_issues_by_category(request):
    try:
        q = request.GET['q']
    except KeyError:
        q = 'where is my order'

    issues = Issue.objects.filter(category=q).order_by('created_at')
    context = get_default_context(request)
    context['issues'] = issues
    return render(request, 'index.html', context)


def get_issues_by_status(request):
    try:
        q = request.GET['q']
    except KeyError:
        q = 1

    issues = Issue.objects.filter(status=q).order_by('created_at')
    context = get_default_context(request)
    context['issues'] = issues
    return render(request, 'index.html', context)


def resolve_issue(request):
    try:
        comment_id = request.GET['id']
        issue = Issue.objects.get(comment_id=comment_id)
        issue.status = ISSUE_STATUSES['closed']
        issue.save()
        print(comment('Your issue has been resolved. Happy to help!', comment_id))
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
        issue = Issue.objects.get(comment_id=request.GET['q'])
        messages = [each.to_json() for each in replies]
        messages.insert(0, issue.to_json())
    except KeyError:
        return JsonResponse({'message': 'issue id not provided'}, status=200)
    else:
        return JsonResponse(messages, safe=False)
