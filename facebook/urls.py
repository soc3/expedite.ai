from django.conf.urls import url

from facebook.views import hello, live_api_callback

urlpatterns = [
    url(r'^home/', hello),
    url(r'^callback/', live_api_callback)
]
