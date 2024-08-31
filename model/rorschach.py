from datetime import datetime
from serviceable import Serviceable
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery

class Rorschach(Serviceable):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.battery = NubbinBattery(last_service_date, datetime.today().date())

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()
