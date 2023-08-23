from django.db.models import Q
from django.views.generic import ListView
from ..topics.models import Topic


class TopicsListView(ListView):
    model = Topic
    template_name = "topics/topics-main.html"
    context_object_name = "topics"

    def get_queryset(self):
        search_query = self.request.GET.get('q')
        queryset = super().get_queryset()

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query)
            )

        return queryset
