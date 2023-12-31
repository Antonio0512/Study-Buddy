from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic import FormView, DeleteView, ListView

from .models import Message
from ..rooms.models import Room
from ..study_messages.forms import MessageForm


class MessagesListView(ListView):
    model = Message
    template_name = "messages/activity.html"
    context_object_name = "activity_messages"


class MessageAddView(LoginRequiredMixin, FormView):
    form_class = MessageForm

    def form_valid(self, form):
        room = Room.objects.get(pk=self.kwargs.get('pk'))

        message = form.save(commit=False)
        message.room = room
        message.user = self.request.user
        message.save()

        room.participants.add(message.user)

        return redirect('room-details', pk=room.id)


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    template_name = "messages/message-delete.html"

    def get_success_url(self):
        return reverse_lazy("room-details", kwargs={'pk': self.object.room.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        message = self.object

        context['room_id'] = message.room.pk

        return context

    def dispatch(self, request, *args, **kwargs):
        message = self.get_object()

        if message.user != self.request.user:
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)
