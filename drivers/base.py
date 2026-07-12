"""
Base driver for all ELMS instruments.
"""

from abc import ABC, abstractmethod
from typing import Any


class BaseInstrumentDriver(ABC):
    """
    Abstract base class for all instrument drivers.
    """

    def __init__(self, instrument: Any):
        self.instrument = instrument
        self.connected = False

    @abstractmethod
    def connect(self) -> bool:
        """Connect to the instrument."""
        raise NotImplementedError

    @abstractmethod
    def disconnect(self) -> None:
        """Disconnect from the instrument."""
        raise NotImplementedError

    @abstractmethod
    def identify(self) -> str:
        """Return *IDN? response."""
        raise NotImplementedError

    @abstractmethod
    def measure(self, parameter: str | None = None):
        """Perform one measurement."""
        raise NotImplementedError

    def is_connected(self) -> bool:
        """Return current connection state."""
        return self.connected

    @abstractmethod
    def send_command(self, command: str) -> None:
        """
        Send a SCPI command.
        """
        raise NotImplementedError

    @abstractmethod
    def read_response(self):
        """
        Read instrument response.
        """
        raise NotImplementedError

    @abstractmethod
    def query(self, command: str) -> str:
        """
        Send a SCPI query and return the response.
        """
        raise NotImplementedError