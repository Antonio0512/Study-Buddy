from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic import FormView, DeleteView

from .models import Message
from ..rooms.models import Room
from ..study_messages.forms import MessageForm


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
