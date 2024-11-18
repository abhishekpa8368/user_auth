from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    last_login_ip = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return self.username
