
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views

urlpatterns = [
    path('mypage/', include('mypage.urls')),
    path('accounts/', include('accounts.urls')),
    path('main/', include('main.urls')),
    path('', views.index),
    path('parsed_data/', include('parsed_data.urls')),
    path('boards/', include('boards.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)