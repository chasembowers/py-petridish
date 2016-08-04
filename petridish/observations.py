class Observations(object):

    @classmethod
    def of(cls, environment): return cls(environment)

class IdentityObservations(Observations):

    def __init__(self, environment):
        self.environment = environment

    def __eq__(self, other):
        if not isinstance(other, self.__class__): return False
        if self.environment != other.environment: return False
        return True
#
# class Observer(object):
#
#     def observe(self, environment): raise NotImplementedError
#
# class IdentityObserver(Observer):
#
#     def observe(self, environment): return IdentityObservations(environment)
