from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("study_buddy_proj.common.urls")),
    path('room/', include("study_buddy_proj.rooms.urls")),
]
