from django.urls import path
from . import views    # 동일한 디렉토리에 있는 views.py 를 import 하겠다.

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),

]