class GridEnvironment(object):

    def width(self):
        raise NotImplementedError('Must implement Environment interface.')

    def height(self):
        raise NotImplementedError('Must implement Environment interface.')

    def addCell(self, body):
        raise NotImplementedError('Must implement Environment interface.')

    def cells(self):
        raise NotImplementedError('Must implement Environment interface.')

    def timeStep(self):
        raise NotImplementedError('Must implement Environment interface.')


class BasicGridEnvironment(GridEnvironment):

    def __init__(self, width, height):
        self._cells = []
        self._width = width
        self._height = height

    def width(self): return self._width

    def height(self): return self._height

    def addCell(self, body):
        self._cells.append(body)

    def cells(self):
        return self._cells

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

    def _moveInBounds(self, cell):
        if cell.isLeftOf(0):cell.moveRight()
        elif cell.isRightOf(self._width-1): cell.moveLeft()
        if cell.isBelow(0): cell.moveUp()
        elif cell.isAbove(self._height - 1): cell.moveDown()
