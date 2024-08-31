# tire.py
from abc import ABC, abstractmethod

class Tire(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        """Determine if the tires need servicing."""
        pass
