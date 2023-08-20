from django.db.models import Q
from django.views.generic import ListView

from ..rooms.models import Room
from ..topics.models import Topic


class RoomsList(ListView):
    model = Room
    template_name = "common/home.html"
    context_object_name = "rooms"

    def get_context_data(self, *, object_list=None, **kwargs):
        topics = Topic.objects.all()

        context = super().get_context_data(**kwargs)
        context["topics"] = topics

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(topic__name__icontains=search_query) |
                Q(description__icontains=search_query)
            )

        return queryset
