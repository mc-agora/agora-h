from django.urls import path
from . import views    # 동일한 디렉토리에 있는 views.py 를 import 하겠다.

app_name = 'parsed_data'

urlpatterns = [
    path('', views.index, name='index'),
    path('GOV/', views.GOV, name='GOV'),
    path('ASSEM/', views.ASSEM, name='ASSEM'),
    path('ASSEM-REGU/', views.ASSEM_REGU, name='ASSEM_REGU'),
    path('GOV/<int:gov_pk>/', views.GOV_DETAIL, name='gov_detail'),
    path('ASSEM/<int:assem_pk>/', views.ASSEM_DETAIL, name='assem_detail'),
    path('ASSEM-REGU/<int:regu_pk>/', views.REGU_DETAIL, name='regu_detail'),

]