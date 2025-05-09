from abc import ABC, abstractmethod
from pathlib import Path

class Document_reader(ABC):
    @abstractmethod
    def reader(rout:Path)->str:
        pass


