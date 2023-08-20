from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.RoomDetailsView.as_view(), name="room-details"),
    path("<int:pk>/edit/", views.RoomUpdateView.as_view(), name="room-update"),
    path("<int:pk>/delete/", views.RoomDeleteView.as_view(), name="room-delete"),
    path("create/", views.RoomCreateView.as_view(), name="room-create")
]
