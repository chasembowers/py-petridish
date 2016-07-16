class Energized(object):

    def energy(self): raise NotImplementedError('Must implement Energized interface.')

    def consumeEnergy(self, energy): raise NotImplementedError('Must implement Energized interface.')

    def releaseEnergy(self, energy): raise NotImplementedError('Must implement Energized interface.')

class SimpleEnergy(Energized):

    def __init__(self, initialEnergy):
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
