from abc import ABC, abstractmethod
from puppy import Puppy


class PuppyState(ABC):

    @abstractmethod
    def play(self, puppy: Puppy) -> str:
        pass

    @abstractmethod
    def feed(self, puppy: Puppy) -> str:
        pass
