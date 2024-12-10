from puppy import Puppy
from puppy_state import PuppyState


class StatePlay(PuppyState):

    def play(self, puppy: Puppy) -> str:
        return 'You throw the ball again and the puppy excitedly chases it.'

    def eat(self, puppy: Puppy) -> str:
        return 'The puppy is too busy playing with the ball to eat right now.'
