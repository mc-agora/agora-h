from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.conf import settings


class User(AbstractUser):
    PEOPLE = 1
    PROFESSOR = 2
    POLITICS = 3
    SPECIALIST = 4
    JOB_CHOICES = (
        (PEOPLE, 'People'),
        (PROFESSOR, 'Professor'),
        (POLITICS, 'Politics'),
        (SPECIALIST, 'Specialist'),
    )
    Female = 'F'
    Male = 'M'
    GENDER = (
        (Female, 'Female'),
        (Male, 'Male')
    )
    user_id = models.CharField(max_length=20, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    profilepic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    job = models.PositiveSmallIntegerField(choices=JOB_CHOICES, null=True, blank=True)
    age = models.IntegerField(blank=True)
    gender = models.CharField(max_length=1, choices=GENDER, default=Male)


