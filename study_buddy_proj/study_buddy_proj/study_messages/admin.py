from django.contrib import admin
from .models import Messages


@admin.register(Messages)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("user", "room", "message")
