from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from helpdesk.views import index
from helpdesk.views import get_issues_by_category, get_issues_by_status
from helpdesk.views import archive_issue, resolve_issue, reopen_issue, get_chat


urlpatterns = [
    url(r'^home/', index),
    url(r'^issues/category/', get_issues_by_category),
    url(r'^issues/status/', get_issues_by_status),
    url(r'^issues/archive', archive_issue),
    url(r'^issues/resolve', resolve_issue),
    url(r'^issues/reopen', reopen_issue),
    url(r'^chat/get', get_chat),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL)
