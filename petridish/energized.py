from petridish.parent import Parent

class Energized(Parent):

    def energy(self): raise NotImplementedError()

    def consumeEnergy(self, energy): raise NotImplementedError()

    def releaseEnergy(self, energy): raise NotImplementedError()

class EnergyOrgan(Energized, Parent): pass

class EnergyFactory(object):

    def produce(self): raise NotImplementedError()

class SimpleEnergy(Energized):

    def __init__(self, initialEnergy):
        if initialEnergy < 0: raise ValueError('Initial energy must be non-negative.')
        self._myEnergy = initialEnergy

    def energy(self): return self._myEnergy

    def consumeEnergy(self, energy):
        if energy < 0: raise ValueError('Cannot consume negative energy.')
        self._myEnergy += energy

    def releaseEnergy(self, energy):
        if energy > self._myEnergy:
            raise ValueError('Not enough energy')
        if energy < 0:
            raise ValueError('Cannot give negative energy.')
        self._myEnergy -= energy


class SimpleEnergyOrgan(Energized):

    def __init__(self, initialEnergy, childEnergyRatio=.5):
        self._energy = SimpleEnergy(initialEnergy)
        if childEnergyRatio < 0 or childEnergyRatio > 1:
            raise ValueError('Child energy ratio must be between 0 and 1.')
        self._childEnergyRatio = float(childEnergyRatio)

    def energy(self): return self._energy.energy()

    def consumeEnergy(self, energy): self._energy.consumeEnergy(energy)

    def releaseEnergy(self, energy): self._energy.releaseEnergy(energy)

    def child(self):
        initialEnergy = self._energy.energy()
        childEnergy = self._childEnergyRatio * initialEnergy
        self._energy.releaseEnergy(childEnergy)
        return SimpleEnergyOrgan(childEnergy, self._childEnergyRatio)

class SimpleEnergyFactory(EnergyFactory):

    def __init__(self, initialEnergy):
        self._initialEnergy = initialEnergy

    def produce(self): return SimpleEnergy(self._initialEnergy)
