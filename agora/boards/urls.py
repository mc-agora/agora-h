from django.urls import path
from . import views    # 동일한 디렉토리에 있는 views.py 를 import 하겠다.

# 여러 APP이 있을 경우 이름 공간을 분리하기 위해 아래와 같이 app의 이름을 지정한다.
# app_name 쓸 때 소문자로 써야함
app_name = 'boards'

# 경로 설정할 때 마지막에 꼭 '/' 가 들어가야 한다.
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:board_pk>/', views.detail, name='detail'),
    path('<int:board_pk>/delete/', views.delete, name='delete'),
    path('<int:board_pk>/edit/', views.edit, name='edit'),
    path('<int:board_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:board_pk>/comments/<int:comment_pk>/edit/', views.comments_edit, name='comments_edit'),
    path('<int:board_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:board_pk>/like/', views.like, name='like'),
    path('<int:board_pk>/follow/<int:user_pk>/', views.follow, name='follow'),
]