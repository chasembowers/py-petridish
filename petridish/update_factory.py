from petridish.update import Move


class UpdateFactory(object):

    def produce(self, cellLocation): raise NotImplementedError

class MoveFactory(UpdateFactory):

    def __init__(self, displacement, cost):

        self._displacement = displacement
        self._cost = cost

    def produce(self, cellLocation): return Move(cellLocation, self._displacement, self._cost)