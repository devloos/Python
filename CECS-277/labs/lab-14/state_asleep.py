from puppy_state import PuppyState


class StateAsleep(PuppyState):

    def play(self, puppy) -> str:
        return "The puppy is asleep. It doesn't want to play right now."

    def feed(self, puppy) -> str:
        from state_eat import StateEat

        puppy.change_state(StateEat())
        return 'The puppy wakes up and comes running to eat.'
