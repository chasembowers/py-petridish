from petridish.actor import Actor
from petridish.energized import Energized, SimpleEnergy
from petridish.parent import Parent

class Cell(Energized, Actor, Parent): pass

# class BasicCell(Cell):
#
#     def __init__(self, actor, energized=None):
#         self._actor = actor
#
#         if energized is None: energized = SimpleEnergy(100)
#         self._myEnergy = energized
#
#     def act(self, cells, resources): return self._actor.act(self, cells, resources)
#
#     def energy(self): return self._myEnergy.energy()
#
#     def releaseEnergy(self, energy): self._myEnergy.releaseEnergy(energy)
#
#     def consumeEnergy(self, energy): self._myEnergy.consumeEnergy(energy)
#
#     def child(self):
#         return BasicCell(self._actor.child(), self._myEnergy.child())