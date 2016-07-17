from copy import copy

from petridish.energized import Energized, SimpleEnergy
from petridish.locatable import Locatable
from petridish.movable import Movable
from petridish.parent import Parent
from petridish.point import Point

class Cell(Locatable, Movable, Energized, Parent):

    def act(self, bodies): raise NotImplementedError('Must implement Cell interface.')

class BasicCell(Cell):

    def __init__(self, actor, energized=None, location=None):
        if location is None: location = Point()
        self._location = location
        self._actor = actor

        if energized is None: energized = SimpleEnergy(100)
        self._myEnergy = energized

    def moveRight(self): self._location.moveRight()

    def moveUp(self): self._location.moveUp()

    def moveLeft(self): self._location.moveLeft()

    def moveTo(self, coordinates): self._location.moveTo(coordinates)

    def act(self, cells, resources): return self._actor.act(self, cells, resources)

    def moveDown(self): self._location.moveDown()

    def isRightOf(self, xEquals): return self._location.isRightOf(xEquals)

    def isBelow(self, yEquals): return self._location.isBelow(yEquals)

    def isLeftOf(self, xEquals): return self._location.isLeftOf(xEquals)

    def coordinates(self): return self._location.coordinates()

    def energy(self): return self._myEnergy.energy()

    def isAbove(self, yEquals): return self._location.isAbove(yEquals)

    def releaseEnergy(self, energy): self._myEnergy.releaseEnergy(energy)

    def consumeEnergy(self, energy): self._myEnergy.consumeEnergy(energy)

    def child(self):
        return BasicCell(self._actor.child(), self._myEnergy.child(), copy(self._location))