class Observations(object): pass

class Observer(object):

    def observe(self, environment): raise NotImplementedError

class NullObservations(Observations): pass

class NullObserver(Observer):

    def observe(self, environment): return NullObservations()
