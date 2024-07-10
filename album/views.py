from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from album.models import Album
from .forms import AlbumForm
from django.contrib import messages


class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'create_album.html'
    login_url = 'user.login'
    success_url = reverse_lazy('musician.create')

    def form_valid(self, form):
        messages.success(self.request, 'Album Saved Successfully!!')
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
