from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class User(AbstractUser, models.Model):
    PEOPLE = 1
    PROFESSOR = 2
    POLITICS = 3
    SPECIALIST = 4
    JOB_CHOICES = (
        (PEOPLE, '일반인'),
        (PROFESSOR, '학계'),
        (POLITICS, '정치계'),
        (SPECIALIST, '산업계'),
    )
    Female = '여성'
    Male = '남성'
    GENDER = (
        (Female, '여성'),
        (Male, '남성')
    )

    user_name = models.CharField(max_length=20, blank=False, verbose_name='성명', null=False)
    birthdate = models.DateField(null=False, blank=False, verbose_name='생년월일')
    profilepic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg', verbose_name='프로필 이미지')
    job = models.PositiveSmallIntegerField(choices=JOB_CHOICES, null=True, blank=True, verbose_name='영역')
    age = models.PositiveIntegerField(default=20, validators=[MinValueValidator(18), MaxValueValidator(100)], blank=False, verbose_name='나이')
    gender = models.CharField(max_length=2, choices=GENDER, default=Male, verbose_name='성별')
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')
    text = models.TextField(blank=False, null=False, verbose_name='자기소개')

