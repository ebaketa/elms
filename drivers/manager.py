from .mock import MockDriver


class DriverManager:

    @staticmethod
    def get_driver(instrument):
        """
        Return the correct driver instance.
        """

        # Za sada svi instrumenti koriste MockDriver.
        # Kasnije ćemo ovdje birati Keysight,
        # Rigol, UNI-T, itd.

        return MockDriver(instrument)