from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class UserLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful!!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Username or email did not match!')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('home')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('user.login')

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'Logout successful!!')
        return super().dispatch(request, *args, **kwargs)


class UserRegistrationView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('user.login')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        return form
