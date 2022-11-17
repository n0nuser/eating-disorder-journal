from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.db import models


class CustomUser(AbstractUser):
    gender = [
        ("m", "Male"),
        ("f", "Female"),
        ("o", "Other"),
    ]
    email = models.EmailField(("email address"), unique=True)
    gender = models.CharField(max_length=1, choices=gender, blank=False, null=False)

    def __str__(self) -> str:
        return self.username

    class Meta:
        ordering = ["first_name"]
        verbose_name_plural = "Users"
