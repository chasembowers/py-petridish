class Energized(object):

    def energy(self): raise NotImplementedError('Must implement Energized interface.')

    def consumeEnergy(self, energy): raise NotImplementedError('Must implement Energized interface.')

    def releaseEnergy(self, energy): raise NotImplementedError('Must implement Energized interface.')