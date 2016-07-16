from copy import copy

from petridish.resource_distributor import EqualSplitResourceDistributor
from petridish.resource_spawner import UniformResourceSpawner
from random import randint

class GridEnvironment(object):

    def width(self):
        raise NotImplementedError('Must implement Environment interface.')

    def height(self):
        raise NotImplementedError('Must implement Environment interface.')

    def addCell(self, cell):
        raise NotImplementedError('Must implement Environment interface.')

    def cells(self):
        raise NotImplementedError('Must implement Environment interface.')

    def resources(self):
        raise NotImplementedError('Must implement Environment interface.')

    def timeStep(self):
        raise NotImplementedError('Must implement Environment interface.')

class BasicGridEnvironment(GridEnvironment):

    _defaultCost = {
        None: 1,
        "left": 2,
        "right": 2,
        "up": 2,
        "down": 2
    }

    def __init__(self, width, height, resourceDistributor=None, resourceSpawner=None, cost=None):
        self._cells = []
        self._resources = []
        self._width = width
        self._height = height

        if resourceDistributor is None: resourceDistributor = EqualSplitResourceDistributor()
        self._distributor = resourceDistributor
        if resourceSpawner is None: resourceSpawner = UniformResourceSpawner()
        self._spawner = resourceSpawner
        if cost is None: cost = self._defaultCost
        self._cost = cost

    def width(self): return self._width

    def height(self): return self._height

    def _assertInBounds(self, locatable):
        if \
            locatable.isLeftOf(0) or \
            locatable.isRightOf(self._width-1) or \
            locatable.isBelow(0) or \
            locatable.isAbove(self._height-1):
                raise ValueError('Cannot add Locatable outside grid.')

    def addCell(self, cell, randLocation=False):
        if randLocation:
            x,y = randint(0, self._width - 1), randint(0, self._height - 1)
            cell.moveTo((x,y))
        else: self._assertInBounds(cell)
        self._cells.append(cell)

    def _addResource(self, resource):
        self._assertInBounds(resource)
        self._resources.append(resource)

    def cells(self):
        return self._cells

    def resources(self):
        return self._resources

    def timeStep(self):
        for cell in self._cells:
            action = cell.act(self._cells, self._resources)
            self._doAction(cell, action)
            self._moveInBounds(cell)
        self._distributor.distribute(self._cells, self._resources)
        for resource in self._spawner.spawn(self):
            self._addResource(resource)
        self._removeDead()

    def _doAction(self, cell, action):
        if not action: return
        elif action == 'left': cell.moveLeft()
        elif action == 'right': cell.moveRight()
        elif action == 'up': cell.moveUp()
        elif action == 'down': cell.moveDown()
        else: raise Exception('Not a valid action')
        if action in self._cost: cell.releaseEnergy(self._cost[action])

    def _moveInBounds(self, locatable):
        if locatable.isLeftOf(0):locatable.moveRight()
        elif locatable.isRightOf(self._width-1): locatable.moveLeft()
        if locatable.isBelow(0): locatable.moveUp()
        elif locatable.isAbove(self._height-1): locatable.moveDown()

    def _removeDead(self):
        cellsToRemove = set()
        for cell in self._cells:
            if cell.energy() == 0: cellsToRemove.add(cell)
        self._cells = [x for x in self._cells if x not in cellsToRemove]

        resourcesToRemove = set()
        for resource in self._resources:
            if resource.energy() == 0: resourcesToRemove.add(resource)
        self._resources = [x for x in self._resources if x not in resourcesToRemove]
