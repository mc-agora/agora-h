from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    #path('mypage/', views.userinfo, name='mypage'),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('delete/', views.delete, name="delete"),
    path('edit/', views.edit, name='edit'),
    path('password/', views.change_password, name='change_password'),
]