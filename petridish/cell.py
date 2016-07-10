from petridish.energized import Energized
from petridish.locatable import Locatable
from petridish.movable import Movable
from petridish.point import Point

class Cell(Locatable, Movable, Energized):

    def act(self, bodies): raise NotImplementedError('Must implement Cell interface.')

class BasicCell(Cell):

    def __init__(self, actor, energy, location=None):
        if location is None: location = Point()
        self._location = location
        self._actor = actor
        self._myEnergy = energy

    def moveLeft(self): self._location.moveLeft()

    def moveRight(self): self._location.moveRight()

    def moveUp(self): self._location.moveUp()

    def moveDown(self): self._location.moveDown()

    def act(self, bodies): return self._actor.act(bodies)

    def isLeftOf(self, xEquals): return self._location.isLeftOf(xEquals)

    def isRightOf(self, xEquals): return self._location.isRightOf(xEquals)

    def isBelow(self, yEquals): return self._location.isBelow(yEquals)

    def isAbove(self, yEquals): return self._location.isAbove(yEquals)

    def coordinates(self): return self._location.coordinates()

    def energy(self): return self._myEnergy

    def consumeEnergy(self, energy):
        if energy < 0: raise ValueError('Cannot consume negative energy.')
        self._myEnergy += energy