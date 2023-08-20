from django.views.generic import ListView

from ..rooms.models import Room


class RoomsList(ListView):
    model = Room
    template_name = "common/home.html"
    context_object_name = "rooms"
