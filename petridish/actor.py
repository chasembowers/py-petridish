import random

from petridish.parent import Parent
from petridish.simulator import DEFAULT_ACTIONS


class Actor(Parent):

    def act(self, introspection, observations, cellLocation): raise NotImplementedError()

class RandomActor(Actor):

    def child(self): return RandomActor()

    def act(self, introspection, observations, cellLocation):
        return random.choice(DEFAULT_ACTIONS.keys())