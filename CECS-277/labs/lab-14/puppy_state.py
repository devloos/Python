from abc import ABC, abstractmethod


class PuppyState(ABC):

    @abstractmethod
    def play(self, puppy) -> str:
        pass

    @abstractmethod
    def feed(self, puppy) -> str:
        pass
