from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser)

from django.db import models

# Create your models here.
class User(AbstractBaseUser):
    username = models.CharField(db_index=True, max_length=30, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    first_name = models.CharField(max_length=120, blank=True)
    last_name = models.CharField(max_length=120, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    def __str__(self):

        return self.email
