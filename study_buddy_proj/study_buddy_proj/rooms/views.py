from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from .forms import RoomForm

from ..rooms.models import Room


class RoomsList(ListView):
    model = Room
    template_name = "room/room-list.html"
    context_object_name = "rooms"


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
