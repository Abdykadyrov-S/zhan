from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to="profile_images", blank=True, null=True)
    phone = models.CharField(max_length=50)
    promo_code = models.CharField(max_length=12, blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return self.username


