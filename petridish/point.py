from petridish.locatable import Locatable
from petridish.movable import Movable


class Point(Locatable, Movable):

    def __init__(self, coordinates=(0,0)):
        self._coordinates = coordinates

    def _move(self, x, y):
        self._coordinates = (self._coordinates[0] + x, self._coordinates[1] + y)

    def coordinates(self): return self._coordinates

    def moveLeft(self): self._move(-1, 0)

    def moveRight(self): self._move(1, 0)

    def moveUp(self): self._move(0, 1)

    def moveDown(self): self._move(0, -1)

    def isRightOf(self, xEquals): return self._coordinates[0] > xEquals

    def isLeftOf(self, xEquals): return self._coordinates[0] < xEquals

    def isAbove(self, yEquals): return self._coordinates[1] > yEquals

    def isBelow(self, yEquals): return self._coordinates[1] < yEquals
