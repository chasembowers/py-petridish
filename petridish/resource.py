from petridish.locatable import Locatable
from petridish.point import Point

class Resource(Locatable):

    def energy(self): raise NotImplementedError('Must implement Resource interface.')

    def giveEnergy(self, energy): raise NotImplementedError('Must implement Resource interface.')

class BasicResource(Resource):

    def __init__(self, energy, location=None):

        if location is None: location = Point()
        self._myEnergy = energy
        self._location = location

    def isLeftOf(self, xEquals): return self._location.isLeftOf(xEquals)

    def isRightOf(self, xEquals): return self._location.isRightOf(xEquals)

    def isBelow(self, yEquals): return self._location.isBelow(yEquals)

    def isAbove(self, yEquals): return self._location.isAbove(yEquals)

    def coordinates(self): return self._location.coordinates()

    def energy(self): return self._myEnergy

    def giveEnergy(self, energy):
        if energy > self._myEnergy:
            raise ValueError('Resource does not have enough energy')
        if energy < 0:
            raise ValueError('Cannot give negative energy.')
        self._myEnergy -= energy