import random

class Actor:

    def act(self, myCell, cells, resources): raise NotImplementedError('Must implement Actor interface.')

class NullActor(Actor):

    def act(self, myCell, cells, resources): return None

class RandomActor(Actor):

    def act(self, myCell, cells, resources): return random.choice(['left', 'right', 'up', 'down', ''])
