import random

from petridish.parent import Parent


class Actor(Parent):

    def act(self, myCell, cells, resources): raise NotImplementedError('Must implement Actor interface.')

class RandomActor(Actor):

    def child(self): return self

    def act(self, myCell, cells, resources): return random.choice(['left', 'right', 'up', 'down', 'reproduce', ''])
