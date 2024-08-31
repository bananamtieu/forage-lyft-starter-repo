from datetime import datetime
from serviceable import Serviceable
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery

class Palindrome(Serviceable):
    def __init__(self, last_service_date, warning_light_on):
        self.engine = SternmanEngine(warning_light_on)
        self.battery = SpindlerBattery(last_service_date, datetime.today().date())

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()
