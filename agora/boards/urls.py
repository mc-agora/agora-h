from django.urls import path
from . import views    # 동일한 디렉토리에 있는 views.py 를 import 하겠다.

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:pk>/', views.detail),
    path('<int:pk>/delete/', views.delete),
    path('<int:pk>/edit/', views.edit),
    path('<int:pk>/update/', views.update),
]