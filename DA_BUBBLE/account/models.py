from django.db import models
from django.contrib.auth.models import AbstractUser

class DA_Bubble_User(AbstractUser):
    username = models.CharField(unique=True, max_length=50)
    email = models.EmailField(unique=True)
    avatarname = models.ImageField(upload_to='avatars', blank=False)