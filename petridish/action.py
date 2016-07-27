class Action(object):

    def apply(self, cell, environment): raise NotImplementedError

    def cost(self): raise NotImplementedError()

class MoveUp(Action):

    def __init__(self, cost):
        self._cost = cost

    def apply(self, cell, environment):

        cells = environment.cells
        if cell not in cells: return False
        cellLocation = cells.locationOf(cell)
        newLocation = (cellLocation[0], cellLocation[1] + 1)
        if cells.at(newLocation): return False
        cells.move(cell, newLocation)
        return True

    def cost(self): return self._cost