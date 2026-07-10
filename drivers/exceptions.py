"""
ELMS driver exceptions.
"""


class DriverError(Exception):
    """Base driver exception."""


class ConnectionError(DriverError):
    """Connection failed."""


class CommunicationError(DriverError):
    """Communication failed."""


class MeasurementError(DriverError):
    """Measurement failed."""