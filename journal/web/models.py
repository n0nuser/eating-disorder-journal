from django.db import models


class Journal(models.Model):
    user = models.ForeignKey("authentication.CustomUser", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    ocurred_at = models.DateTimeField(blank=False, null=False)
    number_of_times = models.PositiveIntegerField(blank=False, null=True)
    situation_emotion = models.CharField(max_length=560, blank=False, null=True)
    afterwards_feeling = models.CharField(max_length=560, blank=False, null=True)

    def __str__(self):
        return f"{self.ocurred_at} - {self.situation_emotion:5.50}"

    class Meta:
        verbose_name_plural = "Journal"
        ordering = ["-ocurred_at"]


class Thought(models.Model):
    user = models.ForeignKey("authentication.CustomUser", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    ocurred_at = models.DateTimeField(blank=False, null=False)
    journal = models.ForeignKey(Journal, on_delete=models.DO_NOTHING, blank=True, null=True)
    thought = models.CharField(max_length=560, blank=False, null=True)

    def __str__(self):
        return f"{self.created_at} - {self.user}"

    class Meta:
        ordering = ["-ocurred_at"]


class SportType(models.Model):
    user = models.ForeignKey("authentication.CustomUser", on_delete=models.CASCADE)
    name = models.CharField(max_length=560, blank=False, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]


class Sport(models.Model):
    """Register sport activity"""

    user = models.ForeignKey("authentication.CustomUser", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    ocurred_at = models.DateTimeField(blank=False, null=False)
    sport = models.ForeignKey(SportType, models.DO_NOTHING, max_length=560, blank=False, null=True)
    duration = models.PositiveIntegerField(blank=False, null=True)

    def __str__(self):
        return f"{self.ocurred_at} - {self.sport:5.50}"

    class Meta:
        verbose_name_plural = "Sport"
        ordering = ["-ocurred_at"]


class Food(models.Model):
    """Register food eaten throughout the day"""

    MEALS = [
        ("BF", "Breakfast"),
        ("BR", "Brunch"),
        ("LU", "Lunch"),
        ("SN", "Snack"),
        ("DI", "Dinner"),
        ("OT", "Other"),
    ]
    user = models.ForeignKey("authentication.CustomUser", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    ocurred_at = models.DateTimeField(blank=False, null=True)
    meal = models.CharField(max_length=2, choices=MEALS, blank=False, null=True)
    food = models.CharField(max_length=1000, blank=False, null=True)
    amount = models.PositiveIntegerField(blank=False, null=True)

    def __str__(self):
        return f"{self.ocurred_at} - {self.food:5.50}"

    class Meta:
        verbose_name_plural = "Food"
        ordering = ["-ocurred_at"]


class HealReasons(models.Model):
    """Keep track of the reasons for healing"""

    user = models.ForeignKey("authentication.CustomUser", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=560, blank=False, null=True)

    def __str__(self):
        return f"{self.reason}"

    class Meta:
        ordering = ["-created_at"]


class ProsCons(models.Model):
    """Pros and cons for your eating disorder"""

    TYPES = [("pros", "Pros"), ("cons", "Cons")]

    user = models.ForeignKey("authentication.CustomUser", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=560, blank=False, null=True)
    type = models.CharField(choices=TYPES, max_length=10, blank=False, null=True)

    def __str__(self):
        return f"{self.pros}"

    class Meta:
        ordering = ["-created_at"]


class ForTheBetterLife(models.Model):
    """Write about how life has changed for your recovered self"""

    user = models.ForeignKey("authentication.CustomUser", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=1000, blank=False, null=True)

    def __str__(self):
        return f"{self.text}"

    class Meta:
        ordering = ["-created_at"]


class Measurements(models.Model):
    """Body measurements"""

    user = models.ForeignKey("authentication.CustomUser", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    ocurred_at = models.DateTimeField(blank=False, null=False)
    weight = models.PositiveIntegerField(blank=False, null=True)  # kg
    height = models.PositiveIntegerField(blank=False, null=True)  # cm

    @property
    def bmi(self):
        return self.weight / ((self.height / 100) ** 2)

    @property
    def bmi_evaluation(self):
        general = {
            16.9: "Severe Thinness",
            18.4: "Moderate Thinness",
            24.9: "Normal",
            29.9: "Overweight",
            34.9: "Obese Class I",
            39.9: "Obese Class II",
        }
        return next((value for key, value in general.items() if self.bmi <= key), "Obese Class III")

    def __str__(self):
        return f"{self.weight}"

    class Meta:
        ordering = ["-ocurred_at"]
