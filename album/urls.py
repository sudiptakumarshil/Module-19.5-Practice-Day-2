from django.urls import path
from album.views import AlbumCreateView

urlpatterns = [path('create/', AlbumCreateView.as_view(), name='album.create')]
