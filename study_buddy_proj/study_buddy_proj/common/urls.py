from django.urls import path
from .views import RoomsList

urlpatterns = [
    path("", RoomsList.as_view(), name="rooms-all"),
]
