from abc import ABC, abstractmethod

# Define the abstract Engine class
class Engine(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        """Determine if the engine needs servicing."""
        pass