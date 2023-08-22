from django.shortcuts import render
from django.views.generic import ListView

from study_buddy_proj.topics.models import Topic


class TopicsListView(ListView):
    model = Topic
    template_name = "topics/topics-main.html"
    context_object_name = "topics"

