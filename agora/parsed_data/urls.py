from django.urls import path
from . import views    # 동일한 디렉토리에 있는 views.py 를 import 하겠다.

app_name = 'parsed_data'

urlpatterns = [
    path('', views.index, name='index'),
    path('GOV/', views.GOV, name='GOV'),
    path('ASSEM/', views.ASSEM, name='ASSEM'),
    path('ASSEM-REGU/', views.ASSEM_REGU, name='ASSEM_REGU'),
]