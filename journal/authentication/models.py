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
    birth_date = models.DateField(blank=False, null=False)
    
    @property
    def age(self) -> int:
        import datetime

        if self.birth_date:
            today = datetime.date.today()
            return today.year - self.birth_date.year - (
                (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
            )
        return 0

    def __str__(self) -> str:
        return self.username

    class Meta:
        ordering = ["first_name"]
        verbose_name_plural = "Users"
