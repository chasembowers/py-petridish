from petridish.parent import Parent

class Energized(Parent):

    def energy(self): raise NotImplementedError('Must implement Energized interface.')

    def consumeEnergy(self, energy): raise NotImplementedError('Must implement Energized interface.')

    def releaseEnergy(self, energy): raise NotImplementedError('Must implement Energized interface.')

class SimpleEnergy(Energized):

    def __init__(self, initialEnergy, childEnergyRatio=.5):
        if initialEnergy < 0: raise ValueError('Initial energy must be non-negative.')
        self._myEnergy = initialEnergy
        if childEnergyRatio < 0 or childEnergyRatio > 1:
            raise ValueError('Child energy ratio must be between 0 and 1.')
        self._childEnergyRatio = float(childEnergyRatio)

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

    def child(self):
        initialEnergy = self._myEnergy
        self._myEnergy *= (1 - self._childEnergyRatio)
        return SimpleEnergy(initialEnergy * self._childEnergyRatio, self._childEnergyRatio)

