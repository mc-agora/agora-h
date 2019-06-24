
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('mypage/', include('mypage.urls')),
    path('accounts/', include('accounts.urls')),
    path('main/', include('main.urls')),
    path('parsed_data/', include('parsed_data.urls')),
    path('chat/', include('chat.urls')),
    path('boards/', include('boards.urls')),
    path('admin/', admin.site.urls),
]
