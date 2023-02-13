# from django.conf.urls import url
from django.urls import path
from api.views import GetVideo, api

urlpatterns = [
    # path('home/', index, name="index"),
    path('', api, name="api_view"),
    path('getvideo', GetVideo.as_view(), name="api_get_video"),
]
