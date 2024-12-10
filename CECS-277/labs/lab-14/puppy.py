from puppy_state import PuppyState
from state_asleep import StateAsleep


class Puppy():

    def __init__(self):
        self._plays = 0
        self._feeds = 0
        self._state: PuppyState = StateAsleep()

    @property
    def plays(self) -> int:
        return self._plays

    @property
    def feeds(self) -> int:
        return self._feeds

    def change_state(self, new_state: PuppyState):
        self._state = new_state

    def throw_ball(self) -> str:
        return self._state.play(self)

    def give_food(self) -> str:
        return self._state.feed(self)

    def inc_plays(self):
        self._plays += 1

    def inc_feeds(self):
        self._feeds += 1

    def reset(self):
        self._plays = 0
        self._feeds = 0
