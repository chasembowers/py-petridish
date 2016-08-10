class Grid(object):

    def insert(self, body, location): raise NotImplementedError()

    def remove(self, body): raise NotImplementedError()

    def removeAt(self, location): raise NotImplementedError()

    def locationOf(self, body): raise NotImplementedError()

    def at(self, location): raise NotImplementedError()

    def move(self, body, location): raise NotImplementedError()

    def __iter__(self): raise NotImplementedError()

class FastGrid(Grid):

    def __init__(self):

        self._locationToBody = {}
        self._bodyToLocation = {}

    def insert(self, body, location):

        if body in self._bodyToLocation: raise ValueError('Body has already been placed on Grid.')
        if location in self._locationToBody: raise ValueError('Location is occupied by another Body.')

        self._locationToBody[location] = body
        self._bodyToLocation[body] = location

    def remove(self, body):

        self._assertBodyExists(body)
        location = self._bodyToLocation[body]
        del self._bodyToLocation[body]
        del self._locationToBody[location]

    def removeAt(self, location):
        self._assertLocationOccupied(location)
        body = self._locationToBody[location]
        del self._bodyToLocation[body]
        del self._locationToBody[location]

    def locationOf(self, body):
        self._assertBodyExists(body)
        return self._bodyToLocation[body]

    def at(self, location):
        if location not in self._locationToBody: return None
        return self._locationToBody[location]

    def move(self, body, location):
        self.remove(body)
        self.insert(body, location)

    def __iter__(self): return iter(self._bodyToLocation)

    def __len__(self): return len(self._bodyToLocation)

    def _assertBodyExists(self, body):
        if body not in self._bodyToLocation: raise LookupError('Body has not been placed on Grid.')

    def _assertLocationOccupied(self, location):
        if location not in self._locationToBody: raise LookupError('Location is not occupied.')