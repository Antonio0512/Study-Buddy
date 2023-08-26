from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from .forms import RoomCreateForm
from ..rooms.models import Room
from ..study_messages.forms import MessageForm
from ..study_messages.models import Message


class RoomDetailsView(DetailView):
    model = Room
    template_name = "room/room-details.html"
    context_object_name = "room"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room = self.get_object()
        messages = Message.objects.filter(room=room)
        participants = room.participants.all()[:15]
        context['messages'] = messages
        context['comment_form'] = MessageForm
        context['participants'] = participants
        return context


class RoomCreateView(LoginRequiredMixin, CreateView):
    model = Room
    form_class = RoomCreateForm
    template_name = "room/room-create.html"

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("home")


class RoomUpdateView(LoginRequiredMixin, UpdateView):
    model = Room
    form_class = RoomCreateForm
    template_name = "room/room-update.html"

    def get_success_url(self):
        return reverse_lazy("room-details", kwargs={"pk": self.object.pk})

    def get_object(self, queryset=None):
        return self.model.objects.get(pk=self.kwargs['pk'])

    def dispatch(self, request, *args, **kwargs):
        room = self.get_object()

        if room.host != self.request.user:
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)


class RoomDeleteView(LoginRequiredMixin, DeleteView):
    model = Room
    template_name = "room/room-delete.html"
    context_object_name = "room"

    def get_success_url(self):
        return reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        room = self.get_object()

        if room.host != self.request.user:
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)
