from abc import ABC, abstractmethod

# Define the abstract Engine class
class Engine(ABC):
    @abstractmethod
    def engine_should_be_serviced(self) -> bool:
        """Determine if the engine needs servicing."""
        pass