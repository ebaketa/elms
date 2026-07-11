"""
Instrument service.

High-level operations on laboratory instruments.
"""

from django.utils import timezone

from services.connection_manager import ConnectionManager


class InstrumentService:

    @staticmethod
    def connect(instrument):
        """
        Connect to an instrument and update its status.
        """

        driver = ConnectionManager.connect(instrument)

        instrument.status = "online"
        instrument.last_connected = timezone.now()

        instrument.save(update_fields=[
            "status",
            "last_connected",
        ])

        return driver

    @staticmethod
    def identify(instrument) -> str:
        """
        Identify an instrument and store the result.
        """

        driver = ConnectionManager.connect(instrument)

        identity = driver.identify()

        instrument.last_identification = identity
        instrument.last_connected = timezone.now()

        instrument.save(update_fields=[
            "last_identification",
            "last_connected",
        ])

        return identity
