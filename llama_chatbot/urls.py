from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),  # Include chat app URLs
]
