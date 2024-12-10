from puppy import Puppy
from puppy_state import PuppyState


class StateAsleep(PuppyState):

    def play(self, puppy: Puppy) -> str:
        return "The puppy is asleep. It doesn't want to play right now."

    def eat(self, puppy: Puppy) -> str:
        return 'The puppy wakes up and comes running to eat.'
