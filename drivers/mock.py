"""
Mock instrument driver for ELMS development.
"""

import random
from .base import BaseInstrumentDriver


class MockDriver(BaseInstrumentDriver):
    """
    Simulated instrument driver.

    Used during development when no physical
    instrument is connected.
    """

    def connect(self) -> bool:
        self.connected = True
        return True

    def disconnect(self) -> None:
        self.connected = False

    def identify(self) -> str:
        return "ELMS,MOCK,1.0"

    def measure(self, parameter: str | None = None) -> float:
        """
        Return a simulated measurement.
        """

        if parameter == "voltage":
            return round(random.uniform(4.95, 5.05), 5)

        if parameter == "current":
            return round(random.uniform(0.95, 1.05), 5)

        if parameter == "temperature":
            return round(random.uniform(22.0, 28.0), 2)

        return round(random.uniform(0.0, 10.0), 5)