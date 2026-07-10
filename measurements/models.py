from django.db import models

from instruments.models import Instrument


class Measurement(models.Model):

    instrument = models.ForeignKey(
        Instrument,
        on_delete=models.CASCADE,
        related_name="measurements",
    )

    parameter = models.CharField(
        max_length=50,
    )

    value = models.FloatField()

    unit = models.CharField(
        max_length=20,
    )

    timestamp = models.DateTimeField(
        auto_now_add=True,
    )

    notes = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return (
            f"{self.instrument.name} "
            f"{self.parameter} = "
            f"{self.value} {self.unit}"
        )