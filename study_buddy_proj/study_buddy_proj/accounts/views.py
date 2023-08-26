from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from study_buddy_proj.accounts.forms import UserRegisterForm, UserLoginForm, UserUpdateForm
from study_buddy_proj.rooms.models import Room
from study_buddy_proj.study_messages.models import Message
from study_buddy_proj.topics.models import Topic

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
        messages.error(self.request, "The Username and Password do not match!")
        return super().form_invalid(form)


class UserLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "accounts/user-logout.html"


    def get(self, request, *args, **kwargs):
        return self.render_to_response({})

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')


class ProfileDetailsView(DetailView):
    model = User
    template_name = "accounts/profile-details.html"
    context_object_name = "profile"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.get_object()
        user_topics = Topic.objects.all()[:5]
        user_rooms = Room.objects.filter(host=user)
        user_messages = Message.objects.filter(user=user)
        context["rooms"] = user_rooms
        context["topics"] = user_topics
        context["activity_messages"] = user_messages

        return context


class ProfileUpdateView(UpdateView):
    model = User
    template_name = "base/settings.html"
    form_class = UserUpdateForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse("profile-details", kwargs={'pk': self.object.pk})


class ProfileDeleteView(DeleteView):
    model = User
    template_name = "accounts/profile_delete.html"
    context_object_name = "profile"

    def get_success_url(self):
        return reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        profile = self.get_object()

        if profile != self.request.user:
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)
