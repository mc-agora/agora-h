
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('vote/', include('vote.urls')),
    path('main/', include('main.urls')),
    path('raws/', include('raws.urls')),
    path('chat/', include('chat.urls')),
    path('boards/', include('boards.urls')),
    path('admin/', admin.site.urls),
]
