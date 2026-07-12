class DriverRegistry:

    _drivers = {}

    @classmethod
    def register(cls, name, driver_class):
        cls._drivers[name] = driver_class

    @classmethod
    def get(cls, name):
        return cls._drivers.get(name)

    @classmethod
    def create(cls, instrument):

        print("Driver:", repr(instrument.driver))
        print("Available:", cls._drivers.keys())

        driver_class = cls.get(instrument.driver)

        if driver_class is None:
            raise ValueError(
                f"Unknown driver: {instrument.driver}"
            )

        return driver_class(instrument)