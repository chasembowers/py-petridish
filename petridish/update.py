from operator import add
import random

class Update(object):

    def apply(self, environment): raise NotImplementedError

class Move(Update):

    def __init__(self, cellLocation, displacement, cost):

        self._cellLocation = cellLocation
        self._displacement = displacement
        self._cost = cost

    def apply(self, environment):

        cell = environment.at(self._cellLocation, 'cells')

        if not cell: return False
        newLocation = tuple(map(add, self._cellLocation, self._displacement))
        if environment.at(newLocation, 'cells'): return False
        if not environment.inBounds(newLocation): return False
        if cell.energy() < self._cost: return False

        environment.move(cell, newLocation)
        cell.releaseEnergy(self._cost)
        return True

    def __eq__(self, other):
        if not isinstance(other, self.__class__): return False
        if self._cellLocation != other._cellLocation: return False
        if self._displacement != other._displacement: return False
        if self._cost != other._cost: return False
        return True

class BinaryResourceSpawner(Update):

    def __init__(self, probSpawn, energyFactory):

        self._probSpawn = probSpawn
        self._factory = energyFactory

    def apply(self, environment):

        if random.random() < self._probSpawn:
            location = environment.randomLocation()
            resource = self._factory.produce()
            if not environment.at(location, 'resources'): environment.insert('resources', resource, location)