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

    def measure(self, parameter: str = "voltage"):

        if parameter == "voltage":
            return {
                "parameter": "Voltage DC",
                "value": round(random.uniform(4.99, 5.01), 5),
                "unit": "V",
            }

        if parameter == "current":
            return {
                "parameter": "Current DC",
                "value": round(random.uniform(0.99, 1.01), 5),
                "unit": "A",
            }

        return {
            "parameter": parameter,
            "value": 0.0,
            "unit": "",
        }

    def send_command(self, command: str) -> str:

        command = command.strip().upper()

        if command == "*IDN?":
            return "ELMS,MOCK,1.0"

        if command == "MEAS:VOLT?":
            return "5.00012"

        if command == "*RST":
            return "OK"

        return "ERROR: Unknown command"

    @staticmethod
    def send_command(instrument, command):

        driver = ConnectionManager.connect(instrument)

        return driver.send_command(command)

    def instrument_console(request, pk):

        instrument = get_object_or_404(Instrument, pk=pk)

        response = ""

        if request.method == "POST":

            command = request.POST.get("command", "")

            response = InstrumentService.send_command(
                instrument,
                command,
            )

        return render(
            request,
            "instruments/console.html",
            {
                "instrument": instrument,
                "response": response,
            },
        )