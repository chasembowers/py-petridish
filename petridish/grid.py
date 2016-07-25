class Grid(object):

    def insert(self, body, location): raise NotImplementedError()

    def remove(self, body): raise NotImplementedError()

    def removeAt(self, location): raise NotImplementedError()

    def locationOf(self, body): raise NotImplementedError()

    def at(self, location): raise NotImplementedError()

    def width(self): raise NotImplementedError()

    def height(self): raise NotImplementedError()

    def __iter__(self): raise NotImplementedError

class FastGrid(Grid):

    def __init__(self, width, height):

        self._width = width
        self._height = height
        self._locationToBody = {}
        self._bodyToLocation = {}

    def width(self): return self._width

    def height(self): return self._height

    def insert(self, body, location):

        if type(location) is not tuple or len(location) is not 2: raise TypeError('Location must be a 2-tuple.')
        x,y = location
        if x < 0 or x >= self._width or y < 0 or y >= self._height: raise ValueError('Location out of bounds')
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
        self._assertLocationOccupied(location)
        return self._locationToBody[location]

    def move(self, body, location):
        self.remove(body)
        self.insert(body, location)

    def __iter__(self): return iter(self._bodyToLocation)

    def _assertBodyExists(self, body):
        if body not in self._bodyToLocation: raise LookupError('Body has not been placed on Grid.')

    def _assertLocationOccupied(self, location):
        if location not in self._locationToBody: raise LookupError('Location is not occupied.')