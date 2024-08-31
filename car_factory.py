from car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire
from datetime import date

class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_array):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTire(tire_wear_array)  # Assuming Calliope uses Carrigan tires
        return Car(engine, battery, tires)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_array):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = OctoprimeTire(tire_wear_array)  # Assuming Glissade uses Octoprime tires
        return Car(engine, battery, tires)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, tire_wear_array):
        engine = SternmanEngine(warning_light_on)
        battery = NubbinBattery(last_service_date, current_date)
        tires = CarriganTire(tire_wear_array)  # Assuming Palindrome uses Carrigan tires
        return Car(engine, battery, tires)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_array):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = OctoprimeTire(tire_wear_array)  # Assuming Rorschach uses Octoprime tires
        return Car(engine, battery, tires)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_array):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = CarriganTire(tire_wear_array)  # Assuming Thovex uses Carrigan tires
        return Car(engine, battery, tires)
