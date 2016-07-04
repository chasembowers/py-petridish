import random

class Actor:

    def act(self, bodies): raise NotImplementedError('Must implement Actor interface.')

class NullActor(Actor):

    def act(self, bodies): return None

class RandomActor(Actor):

    def act(self, bodies): return random.choice(['left', 'right', 'up', 'down', ''])
