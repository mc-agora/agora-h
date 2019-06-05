from django.db import models

# Create your models here.
class Board(models.Model):

    # Field 정의
    title = models.CharField(max_length=10) # 최대 입력 가능한 글자의 수 제한 여기서는 10글자
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 처음 생성한 시간을 나타냄 (최초 한 번만 생성)
    updated_at = models.DateTimeField(auto_now=True)      # 수정한 시간을 나타냄

    def __str__(self):  # -> __ 함수명 __ 이러한 형태의 메소드는 매직메소드라고 한다.
        return f'{self.id}번글 - {self.title} : {self.content}'
