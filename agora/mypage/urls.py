from django.urls import path
from . import views

app_name = 'mypage'

urlpatterns = [
    path('userprofile/<int:user_pk>/', views.userprofile, name='userprofile'),
]