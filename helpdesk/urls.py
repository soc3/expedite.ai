from django.conf.urls import url
from django.conf import settings

from helpdesk.views import get_issues


urlpatterns = [
    url(r'^issues/', get_issues)
]
