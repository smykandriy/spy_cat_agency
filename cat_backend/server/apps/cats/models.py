from django.db import models
from rest_framework.exceptions import ValidationError


class SpyCat(models.Model):
    name = models.CharField()
    years_of_experience = models.PositiveIntegerField()
    breed = models.CharField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.name}, {self.breed}"


class Target(models.Model):
    name = models.CharField()
    country = models.CharField()
    notes = models.TextField(blank=True)
    complete = models.BooleanField(default=False)

    mission = models.ForeignKey(
        "Mission", related_name="assigned_targets", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Target: {self.name}, {self.complete}"


class Mission(models.Model):
    cat = models.ForeignKey(
        SpyCat,
        related_name="assigned_missions",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    complete = models.BooleanField(default=False)
    targets = models.ManyToManyField(Target, related_name="missions")

    def __str__(self):
        return f"Mission for {self.cat.name if self.cat else 'Unassigned Cat'}"

    def delete(self, *args, **kwargs):
        if self.cat is not None:
            raise ValidationError("Cannot delete a mission that is assigned to a cat.")
        super().delete(*args, **kwargs)
