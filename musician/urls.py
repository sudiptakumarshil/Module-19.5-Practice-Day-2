from django.urls import path
from musician.views import MusicianCreateView, MusicianUpdateView

urlpatterns = [
    path('create/', MusicianCreateView.as_view(), name='musician.create'),
    path('update/<int:id>/', MusicianUpdateView.as_view(), name='musician.update')
]
