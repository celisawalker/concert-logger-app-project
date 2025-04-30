from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('concerts/', views.concert_index, name='concert-index'),
    path('concerts/<int:concert_id>/', views.concert_detail, name='concert-detail'),
    path('concerts/create/', views.ConcertCreate.as_view(), name='concert-create'),
    path('concerts/<int:pk>/update/', views.ConcertUpdate.as_view(), name='concert-update'),
    path('concerts/<int:pk>/delete/', views.ConcertDelete.as_view(), name='concert-delete'),
    path('artists/create/', views.ArtistCreate.as_view(), name='artist-create'),
    path('artists/<int:pk>/', views.ArtistDetail.as_view(), name='artist-detail'),
    path('artists/', views.ArtistList.as_view(), name='artist-index'),
    path('artists/<int:pk>/update/', views.ArtistUpdate.as_view(), name='artist-update'),
    path('artists/<int:pk>/delete/', views.ArtistDelete.as_view(), name='artist-delete'),
]