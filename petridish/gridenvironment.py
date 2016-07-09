class GridEnvironment(object):

    def width(self):
        raise NotImplementedError('Must implement Environment interface.')

    def height(self):
        raise NotImplementedError('Must implement Environment interface.')

    def addCell(self, cell):
        raise NotImplementedError('Must implement Environment interface.')

    def cells(self):
        raise NotImplementedError('Must implement Environment interface.')

    def addResource(self, resource):
        raise NotImplementedError('Must implement Environment interface.')

    def resources(self):
        raise NotImplementedError('Must implement Environment interface.')

    def timeStep(self):
        raise NotImplementedError('Must implement Environment interface.')


class BasicGridEnvironment(GridEnvironment):

    def __init__(self, width, height):
        self._cells = []
        self._resources = []
        self._width = width
        self._height = height

    def width(self): return self._width

    def height(self): return self._height

    def _assertInBounds(self, locatable):
        if \
            locatable.isLeftOf(0) or \
            locatable.isRightOf(self._width-1) or \
            locatable.isBelow(0) or \
            locatable.isAbove(self._height-1):
                raise  ValueError('Cannot add Locatable outside grid.')

    def addCell(self, cell):
        self._assertInBounds(cell)
        self._cells.append(cell)

    def addResource(self, resource):
        self._assertInBounds(resource)
        self._resources.append(resource)

    def cells(self):
        return self._cells

    def resources(self):
        return self._resources

    def timeStep(self):
        for cell in self._cells:
            action = cell.act(self._cells)
            self._doAction(cell, action)
            self._moveInBounds(cell)

    def _doAction(self, body, action):
        if not action: return
        elif action == 'left': body.moveLeft()
        elif action == 'right': body.moveRight()
        elif action == 'up': body.moveUp()
        elif action == 'down': body.moveDown()
        else: raise Exception('Not a valid action')

    def _moveInBounds(self, locatable):
        if locatable.isLeftOf(0):locatable.moveRight()
        elif locatable.isRightOf(self._width-1): locatable.moveLeft()
        if locatable.isBelow(0): locatable.moveUp()
        elif locatable.isAbove(self._height-1): locatable.moveDown()
