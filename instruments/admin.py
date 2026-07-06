from django.contrib import admin

# Register your models here.
from .models import Instrument


@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):

    list_display = (
        "manufacturer",
        "model",
        "name",
        "category",
        "interface",
        "status",
    )

    list_filter = (
        "category",
        "status",
        "interface",
    )

    search_fields = (
        "manufacturer",
        "model",
        "serial_number",
        "name",
    )

    ordering = (
        "manufacturer",
        "model",
    )