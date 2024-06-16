from django.urls import path
from .views import (MusicianListView, MusicianDetailView, MusicianCreateView, MusicianUpdateView, MusicianDeleteView,
                    AlbumCreateView, AlbumUpdateView, AlbumDeleteView)

urlpatterns = [
    path('', MusicianListView.as_view(), name='musician_list'),
    path('musician/<int:pk>/', MusicianDetailView.as_view(), name='musician_detail'),
    path('musician/add/', MusicianCreateView.as_view(), name='musician_add'),
    path('musician/<int:pk>/edit/', MusicianUpdateView.as_view(), name='musician_edit'),
    path('musician/<int:pk>/delete/', MusicianDeleteView.as_view(), name='musician_delete'),
    path('album/add/', AlbumCreateView.as_view(), name='album_add'),
    path('album/<int:pk>/edit/', AlbumUpdateView.as_view(), name='album_edit'),
    path('album/<int:pk>/delete/', AlbumDeleteView.as_view(), name='album_delete'),
]
