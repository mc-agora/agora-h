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

    def __str__(self):  # -> __ 함수명 __ 이러한 형태의 메소드는 매직메소드라고 한다.
        return f'{self.id}번글 - {self.title} : {self.content}'



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
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'<Board{self.board_id}: Comment({self.id} - {self.content})>'

