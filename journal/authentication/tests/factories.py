from django.db import models
from django.test import TestCase
from faker import Factory
import factory

from authentication.models import CustomUser


class CustomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser

    email = factory.Faker("email")
    password = factory.Faker("password")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    username = factory.Faker("user_name")
    gender = factory.Faker("random_element", elements=("m", "f", "o"))
    birth_date = factory.Faker("date_of_birth", minimum_age=18, maximum_age=100)
    is_active = True
    is_staff = False
    is_superuser = False
