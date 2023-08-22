from django.urls import path
from . import views

urlpatterns = [
    path("main-page/", views.TopicsListView.as_view(), name='topics-main')
]
