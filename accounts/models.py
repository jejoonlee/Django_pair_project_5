from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    gender_choice = (
        ('male', 'male'),
        ('female', 'female'),
    )

    profile_name = models.CharField(max_length=80)
    profile_image = models.ImageField(upload_to='image/profile_image', blank=True)
    gender = models.CharField(max_length=20, choices=gender_choice)
    pass