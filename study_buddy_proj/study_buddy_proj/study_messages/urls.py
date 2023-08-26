from django.urls import path

from . import views

urlpatterns = [
    path("<int:pk>/add-message/", views.MessageAddView.as_view(), name="message-add"),
    path("<int:pk>/delete-message/", views.MessageDeleteView.as_view(), name="message-delete"),
    path("all/", views.MessagesListView.as_view(), name="messages-main")
]
