from petridish.energized import Energized, SimpleEnergy
from petridish.parent import Parent

class Cell(Energized, Parent):

    def act(self, observations, myLocation): raise NotImplementedError()

class BasicCell(Cell):

    def __init__(self, actor, energized=None, introspector=None):
        self._actor = actor
        self._introspector = introspector

        if energized is None: energized = SimpleEnergy(100)
        self._myEnergy = energized

    def act(self, observations, myLocation):
        introspection = self._introspector.introspect(self)
        return self._actor.act(introspection, observations, myLocation)

    def energy(self): return self._myEnergy.energy()

    def releaseEnergy(self, energy): self._myEnergy.releaseEnergy(energy)

    def consumeEnergy(self, energy): self._myEnergy.consumeEnergy(energy)

    def child(self):
        return BasicCell(self._actor.child(), self._myEnergy.child(), self._introspector)

    def __eq__(self, other):
        if not isinstance(other, self.__class__): return False
        if self._actor != other._actor: return False
        if self._introspector != other._introspector: return False
        if self._myEnergy != other._myEnergy: return False
        return True