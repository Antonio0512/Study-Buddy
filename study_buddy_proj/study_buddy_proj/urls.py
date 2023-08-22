from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("study_buddy_proj.common.urls")),
    path('accounts/', include("study_buddy_proj.accounts.urls")),
    path('room/', include("study_buddy_proj.rooms.urls")),
    path('topics/', include("study_buddy_proj.topics.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
