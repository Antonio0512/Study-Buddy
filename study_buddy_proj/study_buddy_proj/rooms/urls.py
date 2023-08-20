from django.urls import path
from . import views
from ..study_messages.views import MessageAddView, MessageDeleteView

urlpatterns = [
    path("create/", views.RoomCreateView.as_view(), name="room-create"),
    path("<int:pk>/", views.RoomDetailsView.as_view(), name="room-details"),
    path("<int:pk>/edit/", views.RoomUpdateView.as_view(), name="room-update"),
    path("<int:pk>/delete/", views.RoomDeleteView.as_view(), name="room-delete"),
    path("<int:pk>/add-message/", MessageAddView.as_view(), name="message-add"),
    path("<int:pk>/delete-message/<int:message_pk>/", MessageDeleteView.as_view(), name="message-delete")
]
