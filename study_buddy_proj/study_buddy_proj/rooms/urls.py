from django.urls import path
from . import views

urlpatterns = [
    path("all-rooms/", views.RoomsList.as_view(), name="rooms-all"),
    path("<int:pk>/room/", views.RoomDetailsView.as_view(), name="room-details"),
    path("create-room/", views.RoomCreateView.as_view(), name="room-create")
]
