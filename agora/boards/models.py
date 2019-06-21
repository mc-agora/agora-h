from django.db import models
from django.conf import settings

class Board(models.Model):
    # Field 정의
    title = models.CharField(max_length=20) # 최대 입력 가능한 글자의 수 제한 여기서는 10글자
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 처음 생성한 시간을 나타냄 (최초 한 번만 생성)
    updated_at = models.DateTimeField(auto_now=True)      # 수정한 시간을 나타냄
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # AUTH_USER_MODEL : 장고가 기본적으로 갖고 있는 유저 모델

    # blank 옵션은 좋아요를 누르지 않은 경우를 생각해서 True로 설정.
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_boards', blank=True)

    def __str__(self):
        return f'글 번호 -> {self.id}, 글 제목 -> {self.title}, 글 내용 -> {self.content}'



class DjangoBoard(models.Model):
    subject = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    mail = models.CharField(max_length=50, blank=True)
    memo = models.CharField(max_length=200, blank=True)
    hits = models.IntegerField(null=True, blank=True)

# 댓글 달기를 위한 class 선언
class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='comments_rn')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'<Board{self.board_id}: Comment({self.id} - {self.content})>'
