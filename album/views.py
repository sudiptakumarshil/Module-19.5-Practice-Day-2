from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
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


class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'create_album.html'
    pk_url_kwarg = 'id'
    login_url = 'user.login'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Album Updated Successfully!!')
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = Album
    template_name = 'delete_album.html'
    login_url = 'user.login'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Blog Deleted Successfully!!')
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
