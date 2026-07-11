"""
Connection manager for ELMS.
"""

from drivers.registry import DriverRegistry


class ConnectionManager:

    _connections = {}

    @classmethod
    def connect(cls, instrument):

        if instrument.id in cls._connections:
            return cls._connections[instrument.id]

        driver = DriverRegistry.create(instrument)
        driver.connect()

        cls._connections[instrument.id] = driver

        return driver

    @classmethod
    def disconnect(cls, instrument):

        driver = cls._connections.get(instrument.id)

        if driver is None:
            return

        driver.disconnect()
        del cls._connections[instrument.id]

    @classmethod
    def get(cls, instrument):
        return cls._connections.get(instrument.id)

    @classmethod
    def is_connected(cls, instrument):
        return instrument.id in cls._connections

    @classmethod
    def disconnect_all(cls):
        """
        Disconnect all active instruments.
        """

        for driver in cls._connections.values():
            driver.disconnect()

        cls._connections.clear()

    @classmethod
    def clear(cls):
        """
        Clear cached connections.
        """

        cls._connections.clear()
