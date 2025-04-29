from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('concerts/', views.concert_index, name='concert-index'),
    path('concerts/<int:concert_id>/', views.concert_detail, name='concert-detail'),
    path('concerts/create', views.ConcertCreate.as_view(), name='concert-create'),
]