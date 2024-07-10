from django.urls import path
from musician.views import MusicianCreateView

urlpatterns = [
    path('create/', MusicianCreateView.as_view(), name='musician.create')
]
