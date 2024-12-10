from puppy_state import PuppyState


class StateEat(PuppyState):

    def play(self, puppy) -> str:
        from state_play import StatePlay

        puppy.change_state(StatePlay())
        return 'The puppy looks up from its food and chases the ball you threw.'

    def feed(self, puppy) -> str:
        from state_asleep import StateAsleep

        if puppy.feeds >= 2:
            puppy.change_state(StateAsleep())
            return 'The puppy ate so much it fell asleep!'

        puppy.inc_feeds()
        return 'The puppy continues to eat as you add another scoop of kibble to its bowl.'
