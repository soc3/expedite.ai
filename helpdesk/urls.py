from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from helpdesk.views import get_issues


urlpatterns = [
    url(r'^issues/', get_issues)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL)
