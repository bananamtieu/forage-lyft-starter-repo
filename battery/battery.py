from abc import ABC, abstractmethod

# Define the abstract Battery class
class Battery(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        """Determine if the battery needs servicing."""
        pass
