from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.conf import settings

class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
from django.core.validators import MaxValueValidator, MinValueValidator

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

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

    username = models.CharField(error_messages={'unique': '이미 존재하는 아이디입니다.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, verbose_name='아이디')
    user_name = models.CharField(max_length=20, blank=False, verbose_name='성명')
    image = models.ImageField(upload_to='pic_folder/', verbose_name='프로필 이미지')
    job = models.PositiveSmallIntegerField(choices=JOB_CHOICES, null=True, blank=True, verbose_name='영역')
    gender = models.CharField(max_length=2, choices=GENDER, default=Male, verbose_name='성별')
    text = models.TextField(blank=False, null=False, verbose_name='자기소개')
    date_of_birth = models.DateField(null=False, blank=False, verbose_name='생년월일')

    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin