from operator import add


class Update(object):

    def apply(self, environment): raise NotImplementedError

class Move(Update):

    _DIRECTIONS = {
        'up': (0, 1),
        'down': (0, -1),
        'left': (-1, 0),
        'right': (1, 0)
    }

    def __init__(self, cellLocation, direction, cost):

        self._cellLocation = cellLocation
        self._locationDelta = self._DIRECTIONS[direction]
        self._cost = cost

    def apply(self, environment):

        cells = environment.cells
        cell = cells.at(self._cellLocation)

        if not cell: return False
        newLocation = tuple(map(add, self._cellLocation, self._locationDelta))
        if cells.at(newLocation): return False
        if cell.energy() < self._cost: return False

        cells.move(cell, newLocation)
        cell.releaseEnergy(self._cost)
        return True

    def __eq__(self, other):
        if not isinstance(other, self.__class__): return False
        if self._cellLocation != other._cellLocation: return False
        if self._locationDelta != other._locationDelta: return False
        if self._cost != other._cost: return False
        return True