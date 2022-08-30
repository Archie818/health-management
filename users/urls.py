# from django.conf.urls import url
from django.urls import path
from users.views import ApiView, ApiViewDetail, api_info_create, index, api_info

urlpatterns = [
    path('home/', index, name="index"),
    path('', index, name="index"),
    path('api/', api_info, name="api_view"),
    path('api/create/', api_info_create, name="api_view_create"),
    path('api/view/', ApiView.as_view(), name="api_view_class"),
    path('api/view/<int:pk>/', ApiViewDetail.as_view(),
         name="api_view_detail"),
]
