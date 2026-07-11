"""
Keysight 34461A Digital Multimeter Driver
"""

import time

from drivers.base import BaseInstrumentDriver


class Keysight34461ADriver(BaseInstrumentDriver):
    """
    Driver for Keysight 34461A using Linux USBTMC.
    """

    def __init__(self, instrument):

        super().__init__(instrument)

        self.device = None

    def connect(self):
        """
        Connect to the instrument.
        """

        if self.connected:
            return True

        self.device = open(
            self.instrument.address,
            "rb+",
            buffering=0,
        )

        #
        # Initialize instrument
        #

        self.send_command("*CLS\n")
        time.sleep(0.5)

        self.send_command("DISP:STAT OFF\n")
        time.sleep(0.5)

        self.send_command("CONF:VOLT:DC 10\n")
        time.sleep(0.1)

        self.send_command("VOLT:DC:NPLC 100\n")
        time.sleep(0.1)

        self.connected = True

        return True

    def disconnect(self):
        """
        Disconnect from instrument.
        """

        if self.device:

            self.send_command("DISP:STAT ON\n")
            time.sleep(0.5)

            self.device.close()

            self.device = None

        self.connected = False

    def send_command(self, command):
        """
        Send SCPI command.
        """

        self.device.write(command.encode())

    def read_response(self, size=400):
        """
        Read response from instrument.
        """

        return (
            self.device
            .read(size)
            .decode(errors="replace")
            .strip()
        )

    def identify(self):
        """
        Read *IDN? string.
        """

        self.send_command("*IDN?\n")

        time.sleep(0.5)

        return self.read_response()

    def measure(self, parameter="voltage"):
        """
        Read one measurement.
        """

        if parameter != "voltage":
            raise ValueError(
                f"Unsupported parameter: {parameter}"
            )

        self.send_command("READ?\n")

        #
        # 100 PLC measurement
        #

        time.sleep(5)

        return float(
            self.read_response()
        )