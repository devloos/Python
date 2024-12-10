from puppy import Puppy
from puppy_state import PuppyState


class StateEat(PuppyState):

    def play(self, puppy: Puppy) -> str:
        return 'The puppy looks up from its food and chases the ball you threw.'

    def eat(self, puppy: Puppy) -> str:
        return 'The puppy continues to eat as you add another scoop of kibble to its bowl.'
