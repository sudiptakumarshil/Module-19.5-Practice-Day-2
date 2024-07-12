from django.urls import path
from album.views import AlbumCreateView, AlbumDeleteView, AlbumUpdateView

urlpatterns = [
    path('create/', AlbumCreateView.as_view(), name='album.create'),
    path('edit/<int:id>/', AlbumUpdateView.as_view(), name='album.edit'),
    path('delete/<int:id>/', AlbumDeleteView.as_view(), name='album.delete')
]
