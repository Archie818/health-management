# from django.conf.urls import url
from django.urls import path
from users.views import ApiView, ApiViewDetail, api_info_create, diff_age, index, api_info

urlpatterns = [
    path('', index, name="index"),
    path('diff-age', diff_age, name="diff-age"),
]
