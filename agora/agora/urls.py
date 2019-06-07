
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('chat/', include('chat.urls')),
    path('accounts/', include('accounts.urls')),
    path('boards/', include('boards.urls')),
    path('admin/', admin.site.urls),
]
