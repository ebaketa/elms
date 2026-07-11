"""
Measurement service.
"""

from services.connection_manager import ConnectionManager
from measurements.models import Measurement


class MeasurementService:

    @staticmethod
    def measure(instrument, parameter="voltage"):

        driver = ConnectionManager.connect(instrument)

        value = driver.measure(parameter)

        measurement = Measurement.objects.create(
            instrument=instrument,
            parameter=parameter,
            value=value,
            unit="V",
        )

        return measurement