from django.urls import path
from . import urls

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
]