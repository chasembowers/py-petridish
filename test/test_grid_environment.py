import unittest
from mock import MagicMock

from petridish.grid_environment import BasicGridEnvironment
from petridish.cell import Cell
from petridish.resource import Resource
from petridish.resource_distributor import ResourceDistributor
from petridish.resource_spawner import ResourceSpawner


class TestBasicGridEnvironment(unittest.TestCase):

    _WIDTH = 123
    _HEIGHT = 456
    _CELL_ENERGY = 39
    _RESOURCE_ENERGY = 98

    def setUp(self):

        self._distributor = ResourceDistributor()
        self._distributor.distribute = MagicMock()

        self._spawner = ResourceSpawner()
        self._spawner.spawn = MagicMock()

        self._env = BasicGridEnvironment(self._WIDTH, self._HEIGHT, self._distributor, self._spawner)

        self._cell = Cell()
        self._cell.moveLeft = MagicMock()
        self._cell.moveRight = MagicMock()
        self._cell.moveUp = MagicMock()
        self._cell.moveDown = MagicMock()
        self._cell.isLeftOf = MagicMock(return_value=False)
        self._cell.isRightOf = MagicMock(return_value=False)
        self._cell.isBelow = MagicMock(return_value=False)
        self._cell.isAbove = MagicMock(return_value=False)
        self._cell.act = MagicMock(return_value=None)
        self._cell.energy = MagicMock(return_value=self._CELL_ENERGY)

        self._resource = Resource()
        self._resource.isLeftOf = MagicMock(return_value=False)
        self._resource.isRightOf = MagicMock(return_value=False)
        self._resource.isBelow = MagicMock(return_value=False)
        self._resource.isAbove = MagicMock(return_value=False)
        self._resource.energy = MagicMock(return_value=self._RESOURCE_ENERGY)

        self._env.addCell(self._cell)

    def test_addCells(self):
        cellsToAdd = 5
        cellsBefore = len(self._env.cells())
        for i in range(cellsToAdd): self._env.addCell(self._cell)
        cellsAfter = len(self._env.cells())
        assert cellsAfter - cellsBefore == cellsToAdd

    def test_addResources(self):
        resourcesToAdd = 8
        resourcesBefore = len(self._env.resources())
        for i in range(resourcesToAdd): self._env._addResource(self._resource)
        resourcesAfter = len(self._env.resources())
        assert resourcesAfter - resourcesBefore == resourcesToAdd

    def moveHelper(self, direction):
        self._cell.act = MagicMock(return_value=direction)
        self._env.timeStep()
        if direction == 'left': self._cell.moveLeft.assert_called_with()
        elif direction == 'right': self._cell.moveRight.assert_called_with()
        elif direction == 'up': self._cell.moveUp.assert_called_with()
        elif direction == 'down': self._cell.moveDown.assert_called_with()

    def test_moveLeft(self): self.moveHelper('left')

    def test_moveRight(self): self.moveHelper('right')

    def test_moveUp(self): self.moveHelper('up')

    def test_moveDown(self): self.moveHelper('down')

    def test_outOfLeftBound(self):
        self._cell.isLeftOf = MagicMock(side_effect=lambda x: x == 0)
        self._env.timeStep()
        self._cell.moveRight.assert_called_with()

    def test_outOfRightBound(self):
        self._cell.isRightOf = MagicMock(side_effect=lambda x: x == self._WIDTH - 1)
        self._env.timeStep()
        self._cell.moveLeft.assert_called_with()

    def test_outOfLowerBound(self):
        self._cell.isBelow = MagicMock(side_effect=lambda x: x == 0)
        self._env.timeStep()
        self._cell.moveUp.assert_called_with()

    def test_outOfUpperBound(self):
        self._cell.isAbove = MagicMock(side_effect=lambda x: x == self._HEIGHT - 1)
        self._env.timeStep()
        self._cell.moveDown.assert_called_with()

    def test_addCellOutOfBounds(self):
        self._cell.isLeftOf = MagicMock(side_effect=lambda x: x == 0)
        self.assertRaises(ValueError, self._env.addCell, self._cell)

    def test_addResourceOutOfBounds(self):
        self._resource.isAbove = MagicMock(side_effect=lambda x: x == self._HEIGHT - 1)
        self.assertRaises(ValueError, self._env._addResource, self._resource)

    def test_resourceDistributor(self):
        self._env.timeStep()
        self._distributor.distribute.assert_called_with([self._cell],[])

    def test_resourceSpawner(self):

        self._spawner.spawn = MagicMock(return_value=[self._resource])

        assert self._resource not in self._env.resources()
        self._env.timeStep()
        self._spawner.spawn.assert_called_with(self._env)
        assert self._resource in self._env.resources()

    def test_removesDeadCells(self):
        self._cell.energy = MagicMock(return_value=0)
        assert self._cell in self._env.cells()
        self._env.timeStep()
        assert self._cell not in self._env.cells()

    def test_removesDeadCells(self):
        self._resource.energy = MagicMock(return_value=0)
        self._env._addResource(self._resource)
        assert self._resource in self._env.resources()
        self._env.timeStep()
        assert self._resource not in self._env.resources()

if __name__ == '__main__':
    unittest.main()
