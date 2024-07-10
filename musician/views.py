from django.urls import reverse_lazy
from django.views.generic import CreateView
from musician.models import Musician
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from musician.forms import MusicianForm


# Create your views here.
class MusicianCreateView(LoginRequiredMixin, CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'create_musician.html'
    success_url = reverse_lazy('musician.create')
    login_url = 'user.login'

    def form_valid(self, form):
        messages.success(self.request, 'Musician saved successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
