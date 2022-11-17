import factory
from web.models import Journal, Thought, SportType, Sport, Measurements, Food, ForTheBetterLife, HealReasons, ProsCons


class JournalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Journal

    user = factory.SubFactory("authentication.tests.factories.CustomUserFactory")
    ocurred_at = factory.Faker("date_time_this_month")
    number_of_times = factory.Faker("pyint")
    situation_emotion = factory.Faker("sentence")
    afterwards_feeling = factory.Faker("sentence")


class ThoughtFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Thought

    user = factory.SubFactory("authentication.tests.factories.CustomUserFactory")
    created_at = factory.Faker("date_time_this_month")
    ocurred_at = factory.Faker("date_time_this_month")
    journal = factory.SubFactory(JournalFactory)
    thought = factory.Faker("sentence")


class SportTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SportType

    user = factory.SubFactory("authentication.tests.factories.CustomUserFactory")
    name = factory.Faker("sentence")


class SportFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Sport

    user = factory.SubFactory("authentication.tests.factories.CustomUserFactory")
    created_at = factory.Faker("date_time_this_month")
    ocurred_at = factory.Faker("date_time_this_month")
    sport = factory.SubFactory(SportTypeFactory)
    duration = factory.Faker("pyint")


class MeasurementsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Measurements

    user = factory.SubFactory("authentication.tests.factories.CustomUserFactory")
    created_at = factory.Faker("date_time_this_month")
    ocurred_at = factory.Faker("date_time_this_month")
    weight = factory.Faker("pyint")
    height = factory.Faker("pyint")


MEALS = [
    ("BF", "Breakfast"),
    ("BR", "Brunch"),
    ("LU", "Lunch"),
    ("SN", "Snack"),
    ("DI", "Dinner"),
    ("OT", "Other"),
]


class FoodFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Food

    user = factory.SubFactory("authentication.tests.factories.CustomUserFactory")
    created_at = factory.Faker("date_time_this_month")
    ocurred_at = factory.Faker("date_time_this_month")
    meal = factory.Faker("random_element", elements=MEALS)
    food = factory.Faker("sentence")
    amount = factory.Faker("pyint")


class ForTheBetterLifeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ForTheBetterLife

    user = factory.SubFactory("authentication.tests.factories.CustomUserFactory")
    created_at = factory.Faker("date_time_this_month")
    text = factory.Faker("sentence")


class HealReasonsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = HealReasons

    user = factory.SubFactory("authentication.tests.factories.CustomUserFactory")
    created_at = factory.Faker("date_time_this_month")
    reason = factory.Faker("sentence")


TYPES = [("pros", "Pros"), ("cons", "Cons")]


class ProsConsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProsCons

    user = factory.SubFactory("authentication.tests.factories.CustomUserFactory")
    created_at = factory.Faker("date_time_this_month")
    text = factory.Faker("sentence")
    type = factory.Faker("random_element", elements=TYPES)
