# from django.contrib.auth.models import User, AbstractUser
# from django.db import models
from django.conf import settings
#
# from django.core.validators import MaxValueValidator, MinValueValidator
#
# class User(AbstractUser):
#     PEOPLE = 1
#     PROFESSOR = 2
#     POLITICS = 3
#     SPECIALIST = 4
#     JOB_CHOICES = (
#         (PEOPLE, '일반인'),
#         (PROFESSOR, '학계'),
#         (POLITICS, '정치계'),
#         (SPECIALIST, '산업계'),
#     )
#     Female = 'F'
#     Male = 'M'
#     GENDER = (
#         (Female, '여성'),
#         (Male, '남성')
#     )
#
#     user_name = models.CharField(max_length=20, blank=False, verbose_name='성명')
#     birthdate = models.DateField(null=False, blank=False, verbose_name='생년월일')
#     profilepic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg', verbose_name='프로필 이미지')
#     job = models.PositiveSmallIntegerField(choices=JOB_CHOICES, null=True, blank=True, verbose_name='영역')
#     age = models.PositiveIntegerField(default=20, validators=[MinValueValidator(18), MaxValueValidator(100)], blank=False, verbose_name='나이')
#     gender = models.CharField(max_length=1, choices=GENDER, default=Male, verbose_name='성별')
#     followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')


from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

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
    Female = 'F'
    Male = 'M'
    GENDER = (
        (Female, '여성'),
        (Male, '남성')
    )

    user_name = models.CharField(max_length=20, blank=False, verbose_name='성명')
    profilepic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg', verbose_name='프로필 이미지')
    job = models.PositiveSmallIntegerField(choices=JOB_CHOICES, null=True, blank=True, verbose_name='영역')
    age = models.PositiveIntegerField(default=20, validators=[MinValueValidator(18), MaxValueValidator(100)], blank=False, verbose_name='나이')
    gender = models.CharField(max_length=1, choices=GENDER, default=Male, verbose_name='성별')
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')
    date_of_birth = models.DateField()
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