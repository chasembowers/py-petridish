from operator import add


class Action(object):

    def apply(self, environment, cellLocation, cellArgs): raise NotImplementedError

class Move(Action):

    DIRECTIONS = {
        'up': (0, 1),
        'down': (0, -1),
        'left': (-1, 0),
        'right': (1, 0)
    }

    def __init__(self, cost):
        self._cost = cost

    def apply(self, environment, cellLocation, cellArgs):

        cells = environment.cells
        cell = cells.at(cellLocation)

        if not cell: return False
        newLocation = tuple(map(add, cellLocation, self.DIRECTIONS[cellArgs]))
        if cells.at(newLocation): return False
        if cell.energy() < self._cost: return False

        cells.move(cell, newLocation)
        cell.releaseEnergy(self._cost)
        return True