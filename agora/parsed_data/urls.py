from django.urls import path
from . import views    # 동일한 디렉토리에 있는 views.py 를 import 하겠다.
from django.conf import settings
from django.conf.urls.static import static

app_name = 'parsed_data'

urlpatterns = [
    path('', views.index, name='index'),
    path('GOV/', views.GOV, name='GOV'),
    path('ASSEM/', views.ASSEM, name='ASSEM'),
    path('ASSEM-REGU/', views.ASSEM_REGU, name='ASSEM_REGU'),
    path('GOV/<int:gov_pk>/', views.GOV_DETAIL, name='gov_detail'),
    path('ASSEM/<int:assem_pk>/', views.ASSEM_DETAIL, name='assem_detail'),
    path('ASSEM-REGU/<int:regu_pk>/', views.REGU_DETAIL, name='regu_detail'),
    ################################ GOV ###################################################
    path('GOV/<int:gov_pk>/ga_new/', views.ga_new, name='ga_new'),
    path('GOV/<int:gov_pk>/agree/<int:ga_pk>/', views.ga_agree, name='ga_agree'),
    path('GOV/<int:gov_pk>/gd_new/', views.gd_new, name='gd_new'),
    path('GOV/<int:gov_pk>/disagree/<int:gd_pk>/', views.ga_disagree, name='ga_disagree'),
    ################################# ASSEM ################################################
    path('ASSEM/<int:assem_pk>/aa_new/', views.aa_new, name='aa_new'),
    path('ASSEM/<int:assem_pk>/agree/<int:aa_pk>/', views.aa_agree, name='aa_agree'),
    path('ASSEM/<int:assem_pk>/ad_new/', views.ad_new, name='ad_new'),
    path('ASSEM/<int:assem_pk>/disagree/<int:ad_pk>/', views.aa_disagree, name='aa_disagree'),
    ################################## REGU ################################################
    path('ASSEM-REGU/<int:regu_pk>/ra_new/', views.ra_new, name='ra_new'),
    path('ASSEM-REGU/<int:regu_pk>/agree/<int:ra_pk>/', views.ra_agree, name='ra_agree'),
    path('ASSEM-REGU/<int:regu_pk>/rd_new/', views.rd_new, name='rd_new'),
    path('ASSEM-REGU/<int:regu_pk>/disagree/<int:rd_pk>/', views.ra_disagree, name='ra_disagree'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)