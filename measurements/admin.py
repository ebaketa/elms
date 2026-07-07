from django.contrib import admin

# Register your models here.
from .models import Measurement

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):

    list_display = (
        "instrument",
        "timestamp",
        "function",
        "value",
        "unit",
    )
