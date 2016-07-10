import random
from copy import copy

from petridish.point import Point
from petridish.resource import BasicResource

class ResourceSpawner(object):

    def spawn(self, env):
        raise NotImplementedError('Must implement ResourceSpawner interface.')

class UniformResourceSpawner(ResourceSpawner):

    def __init__(self, energy=10, probSpawn=.1):
        self._energy = energy
        self._probSpawn = probSpawn

    def spawn(self, env):

        newResources = []
        if random.random() < self._probSpawn:

            x = random.randint(0, env.width()-1)
            y = random.randint(0, env.height()-1)
            resourceLocation = Point((x,y))
            newResources.append(BasicResource(self._energy, resourceLocation))

        return newResources