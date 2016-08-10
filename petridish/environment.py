from petridish.grid import FastGrid

class Environment(object):

    def insert(self, group, body, location): raise NotImplementedError()

    def remove(self, body): raise NotImplementedError()

    def locationOf(self, body): raise NotImplementedError()

    def at(self, location, group): raise NotImplementedError()

    def move(self, body, location): raise NotImplementedError()

    def inBounds(self, location): raise NotImplementedError()

    def __getitem__(self, arg): raise NotImplementedError()

class RectangularEnvironment(Environment):

    def __init__(self, width, height, groups=['cells', 'resources']):

        self._width = width
        self._height = height

        if type(groups) is dict: self._groups = groups
        else:
            self._groups = {}
            for group in groups:
                self._groups[group] = FastGrid()

    def insert(self, group, body, location):

        if type(location) is not tuple or len(location) is not 2: raise TypeError('Location must be a 2-tuple.')
        if not self.inBounds(location): raise ValueError('Location out of bounds')

        for grid in self._groups.itervalues():
            if body in grid: raise ValueError('Body already exists in this Environment.')
        self._groups[group].insert(body, location)

    def remove(self, body):
        self._gridWith(body).remove(body)

    def locationOf(self, body):
        return self._gridWith(body).locationOf(body)

    def at(self, location, group):
        grid = self._groups[group]
        return grid.at(location)

    def move(self, body, location):
        self._gridWith(body).move(body, location)

    def inBounds(self, location):
        x,y = location
        return not (x < 0 or x >= self._width or y < 0 or y >= self._height)

    def width(self): return self._width

    def height(self): return self._height

    def __getitem__(self, item):
        return iter(self._groups[item])

    def _gridWith(self, body):
        for grid in self._groups.itervalues():
            if body in grid:
                return grid
        raise LookupError('Body was not found in Environment.')