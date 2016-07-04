from petridish.location import Location
from petridish.actor import Actor, RandomActor


class Cell:

    def __init__(self, location=None, actor=Actor()):
        if location is None: location = Location()
        self._location = location
        self._actor = actor

    def location(self): return self._location

    def moveLeft(self): self._location.moveLeft()

    def moveRight(self): self._location.moveRight()

    def moveUp(self): self._location.moveUp()

    def moveDown(self): self._location.moveDown()

    def act(self, bodies): return self._actor.act(bodies)

    def isLeftOf(self, xEquals): return self._location.isLeftOf(xEquals)

    def isRightOf(self, xEquals): return self._location.isRightOf(xEquals)

    def isBelow(self, yEquals): return self._location.isBelow(yEquals)

    def isAbove(self, yEquals): return self._location.isAbove(yEquals)