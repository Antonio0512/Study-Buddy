from django.contrib import admin
from .models import Room
from .models import Topic


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("name", "topic", "host")


@admin.register(Topic)
class TopicModel(admin.ModelAdmin):
    list_display = ("name",)
