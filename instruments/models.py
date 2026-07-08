from django.db import models

# Create your models here.
class InstrumentCategory(models.TextChoices):
    MULTIMETER = "multimeter", "Multimeter"
    OSCILLOSCOPE = "oscilloscope", "Oscilloscope"
    POWER_SUPPLY = "power_supply", "Power Supply"
    FUNCTION_GENERATOR = "function_generator", "Function Generator"
    MICROCONTROLLER = "microcontroller", "Microcontroller"
    SENSOR = "sensor", "Sensor"
    OTHER = "other", "Other"


class InterfaceType(models.TextChoices):
    USB = "usb", "USB"
    SERIAL = "serial", "Serial"
    LAN = "lan", "LAN"
    GPIB = "gpib", "GPIB"
    MQTT = "mqtt", "MQTT"
    OTHER = "other", "Other"


class InstrumentStatus(models.TextChoices):
    ONLINE = "online", "Online"
    OFFLINE = "offline", "Offline"
    BUSY = "busy", "Busy"
    ERROR = "error", "Error"


class Instrument(models.Model):

    name = models.CharField(max_length=100)

    manufacturer = models.CharField(max_length=100)

    model = models.CharField(max_length=100)

    last_connected = models.DateTimeField(
        null=True,
        blank=True
    )

    last_identification = models.TextField(
        blank=True
    )

    serial_number = models.CharField(
        max_length=100,
        blank=True,
    )

    category = models.CharField(
        max_length=30,
        choices=InstrumentCategory.choices,
        default=InstrumentCategory.OTHER,
    )

    interface = models.CharField(
        max_length=20,
        choices=InterfaceType.choices,
        default=InterfaceType.USB,
    )

    address = models.CharField(
        max_length=255,
        blank=True,
    )

    location = models.CharField(
        max_length=100,
        blank=True,
        help_text="Bench, rack or room location",
    )

    status = models.CharField(
        max_length=20,
        choices=InstrumentStatus.choices,
        default=InstrumentStatus.OFFLINE,
    )

    description = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["manufacturer", "model"]

    def __str__(self):
        return f"{self.manufacturer} {self.model}"

    class Meta:
        ordering = ["manufacturer", "model"]
        verbose_name = "Instrument"
        verbose_name_plural = "Instruments"