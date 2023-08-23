from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.UserRegisterView.as_view(), name='user-register'),
    path("login/", views.UserLoginView.as_view(), name='user-login'),
    path("logout/", views.UserLogoutView.as_view(), name='user-logout'),

    path("<int:pk>/details/", views.ProfileDetailsView.as_view(), name='profile-details'),
    path("<int:pk>/update/", views.ProfileUpdateView.as_view(), name='profile-update'),
    path("<int:pk>/delete/", views.ProfileDeleteView.as_view(), name='profile-delete')
]
