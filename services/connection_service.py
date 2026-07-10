"""
Connection service for ELMS.
"""

from drivers.registry import DriverRegistry
from django.utils import timezone

class ConnectionService:
    """
    Handle instrument connections.
    """

    @staticmethod
    def connect(instrument):
        """
        Create driver and connect to instrument.
        """

        driver = DriverRegistry.create(instrument)

        success = driver.connect()

        return {
            "success": success,
            "driver": driver,
        }

    @staticmethod
    def disconnect(instrument):

        driver = DriverRegistry.create(instrument)

        driver.disconnect()

        return True

    @staticmethod
    def identify(instrument):

        driver = DriverRegistry.create(instrument)

        driver.connect()

        identification = driver.identify()

        driver.disconnect()

        return identification

    @staticmethod
    def identify(instrument):

        driver = ConnectionManager.connect(instrument)

        identity = driver.identify()

        instrument.last_identification = identity
        instrument.last_connected = timezone.now()

        instrument.save(update_fields=[
            "last_identification",
            "last_connected",
        ])

        return identity