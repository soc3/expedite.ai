from django.conf.urls import url

from facebook.views import hello, live_api_callback, comment_on_fb

urlpatterns = [
    url(r'^home/', hello),
    url(r'^callback/', live_api_callback),
    url(r'^comment_on_fb', comment_on_fb)
]
