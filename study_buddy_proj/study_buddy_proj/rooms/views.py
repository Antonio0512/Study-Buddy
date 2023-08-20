from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import RoomForm
from ..rooms.models import Room


class RoomDetailsView(DetailView):
    model = Room
    template_name = "room/room-details.html"
    context_object_name = "room"


class RoomCreateView(CreateView):
    model = Room
    form_class = RoomForm
    template_name = "room/room-form.html"

    def get_success_url(self):
        return reverse("rooms-all")


class RoomUpdateView(UpdateView):
    model = Room
    form_class = RoomForm
    template_name = "room/room-form.html"

    def get_success_url(self):
        return reverse("room-details")

    def get_object(self, queryset=None):
        return self.model.objects.get(pk=self.kwargs['pk'])


class RoomDeleteView(DeleteView):
    model = Room
    template_name = "room/room-delete.html"
    success_url = reverse_lazy("rooms-all")
