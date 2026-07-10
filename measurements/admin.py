from django.contrib import admin

# Register your models here.
from .models import Measurement


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):

    list_display = (
        "instrument",
        "timestamp",
        "parameter",
        "value",
        "unit",
    )

    list_filter = (
        "parameter",
        "timestamp",
    )

    search_fields = (
        "instrument__name",
        "parameter",
    )

    ordering = (
        "-timestamp",
    )