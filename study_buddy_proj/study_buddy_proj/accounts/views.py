from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from study_buddy_proj.accounts.forms import UserRegisterForm, UserLoginForm

User = get_user_model()


class UserRegisterView(CreateView):
    template_name = "accounts/user-register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)

        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(self.request, 'Invalid username or password.')

        login(self.request, user)

        return response


class UserLoginView(LoginView):
    template_name = "accounts/user-login.html"
    form_class = UserLoginForm

    def get_success_url(self):
        return reverse_lazy("home")

    def form_invalid(self, form):
        messages.error(self.request, "Invalid Username or Password!")
        return super().form_invalid(form)
