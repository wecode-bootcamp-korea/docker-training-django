from django.urls import path, include

from basic.views import ping

urlpatterns = [
    path('basic', include('basic.urls')),
    path('ping', ping),
]
