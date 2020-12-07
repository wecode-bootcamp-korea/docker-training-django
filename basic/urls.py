from django.urls import path
from .views      import BasicView

urlpatterns = [
    path('', BasicView.as_view())
]
