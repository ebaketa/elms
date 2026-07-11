from .registry import DriverRegistry
from .mock import MockDriver
from .keysight34461a import Keysight34461ADriver

DriverRegistry.register(
    "mock",
    MockDriver,
)

DriverRegistry.register(
    "keysight34461a",
    Keysight34461ADriver,
)
