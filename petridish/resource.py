from petridish.energized import Energized, SimpleEnergy
from petridish.locatable import Locatable
from petridish.point import Point

class Resource(Locatable, Energized): pass

class BasicResource(Resource):

    def __init__(self, energized, location=None):

        if location is None: location = Point()
        self._myEnergy = energized
        self._location = location

    def isLeftOf(self, xEquals): return self._location.isLeftOf(xEquals)

    def isRightOf(self, xEquals): return self._location.isRightOf(xEquals)

    def isBelow(self, yEquals): return self._location.isBelow(yEquals)

    def isAbove(self, yEquals): return self._location.isAbove(yEquals)

    def coordinates(self): return self._location.coordinates()

    def energy(self): return self._myEnergy.energy()

    def releaseEnergy(self, energy): self._myEnergy.releaseEnergy(energy)