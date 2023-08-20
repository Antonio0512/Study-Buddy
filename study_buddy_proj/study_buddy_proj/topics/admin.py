from django.contrib import admin

from .models import Topic


@admin.register(Topic)
class TopicModel(admin.ModelAdmin):
    list_display = ("name",)
