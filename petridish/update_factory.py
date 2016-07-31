from petridish.update import Move


class UpdateFactory(object):

    def produce(self, cellLocation, toParse): raise NotImplementedError

class MoveFactory(UpdateFactory):

    def __init__(self, cost):

        self._cost = cost

    def produce(self, cellLocation, toParse): return Move(cellLocation, toParse, self._cost)