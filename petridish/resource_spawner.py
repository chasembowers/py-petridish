import random
from copy import copy

from petridish.energized import SimpleEnergy
from petridish.point import Point
from petridish.resource import BasicResource

class ResourceSpawner(object):

    def spawn(self, env):
        raise NotImplementedError('Must implement ResourceSpawner interface.')

class UniformResourceSpawner(ResourceSpawner):

    def __init__(self, energized=None, probSpawn=.1):
        self._probSpawn = probSpawn

        if energized is None: energized = SimpleEnergy(10)
        self._energized = energized

    def spawn(self, env):

        newResources = []
        if random.random() < self._probSpawn:

            x = random.randint(0, env.width()-1)
            y = random.randint(0, env.height()-1)
            resourceLocation = Point((x,y))
            newResources.append(BasicResource(copy(self._energized), resourceLocation))

        return newResources