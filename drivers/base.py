from abc import ABC, abstractmethod


class InstrumentDriver(ABC):
    """
    Base class for all instrument drivers.
    """

    def __init__(self, instrument):
        self.instrument = instrument
        self.connected = False

    @abstractmethod
    def connect(self):
        """Connect to instrument."""
        pass

    @abstractmethod
    def disconnect(self):
        """Disconnect from instrument."""
        pass

    @abstractmethod
    def identify(self):
        """Return instrument identification string."""
        pass

    @abstractmethod
    def measure(self):
        """Perform measurement."""
        pass