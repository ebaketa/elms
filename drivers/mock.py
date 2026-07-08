import random

from .base import InstrumentDriver


class MockDriver(InstrumentDriver):
    """
    Mock instrument driver used for development and testing.
    """

    def connect(self):
        self.connected = True
        return True

    def disconnect(self):
        self.connected = False
        return True

    def identify(self):
        return (
            "ELMS Mock Instrument,"
            "MODEL-001,"
            "SN123456,"
            "1.0"
        )

    def measure(self):
        return {
            "function": "DC Voltage",
            "value": round(random.uniform(4.95, 5.05), 3),
            "unit": "V",
        }