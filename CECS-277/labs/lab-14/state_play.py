from puppy_state import PuppyState


class StatePlay(PuppyState):

    def play(self, puppy) -> str:
        from state_asleep import StateAsleep

        if puppy.plays >= 2:
            puppy.change_state(StateAsleep())
            return 'The puppy played so much it fell asleep!'

        puppy.inc_plays()
        return 'You throw the ball again and the puppy excitedly chases it.'

    def feed(self, puppy) -> str:
        return 'The puppy is too busy playing with the ball to eat right now.'
