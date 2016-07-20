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

        self._cost = {}

        self._env = BasicGridEnvironment(self._WIDTH, self._HEIGHT, self._distributor, self._spawner, self._cost)

        self._cell = Cell()
        self._cell.moveLeft = MagicMock()
        self._cell.moveRight = MagicMock()
        self._cell.moveUp = MagicMock()
        self._cell.moveDown = MagicMock()
        self._cell.moveTo = MagicMock()
        self._cell.isLeftOf = MagicMock(return_value=False)
        self._cell.isRightOf = MagicMock(return_value=False)
        self._cell.isBelow = MagicMock(return_value=False)
        self._cell.isAbove = MagicMock(return_value=False)
        self._cell.act = MagicMock(return_value=None)
        self._cell.energy = MagicMock(return_value=self._CELL_ENERGY)
        self._cell.releaseEnergy = MagicMock()

        self._resource = Resource()
        self._resource.isLeftOf = MagicMock(return_value=False)
        self._resource.isRightOf = MagicMock(return_value=False)
        self._resource.isBelow = MagicMock(return_value=False)
        self._resource.isAbove = MagicMock(return_value=False)
        self._resource.energy = MagicMock(return_value=self._RESOURCE_ENERGY)

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

    def test_addCellAtRandomLocation(self):
        self._env.addCell(self._cell, randLocation=True)

        assert len(self._env.cells()) == 1

        x,y = self._cell.moveTo.call_args[0][0]
        assert x >= 0 and x < self._WIDTH
        assert y >= 0 and y < self._HEIGHT

    def moveHelper(self, direction):
        self._env.addCell(self._cell)
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
        self._env.addCell(self._cell)
        self._cell.isLeftOf = MagicMock(side_effect=lambda x: x == 0)
        self._env.timeStep()
        self._cell.moveRight.assert_called_with()

    def test_outOfRightBound(self):
        self._env.addCell(self._cell)
        self._cell.isRightOf = MagicMock(side_effect=lambda x: x == self._WIDTH - 1)
        self._env.timeStep()
        self._cell.moveLeft.assert_called_with()

    def test_outOfLowerBound(self):
        self._env.addCell(self._cell)
        self._cell.isBelow = MagicMock(side_effect=lambda x: x == 0)
        self._env.timeStep()
        self._cell.moveUp.assert_called_with()

    def test_outOfUpperBound(self):
        self._env.addCell(self._cell)
        self._cell.isAbove = MagicMock(side_effect=lambda x: x == self._HEIGHT - 1)
        self._env.timeStep()
        self._cell.moveDown.assert_called_with()

    def test_addCellOutOfBounds(self):
        self._env.addCell(self._cell)
        self._cell.isLeftOf = MagicMock(side_effect=lambda x: x == 0)
        self.assertRaises(ValueError, self._env.addCell, self._cell)

    def test_addResourceOutOfBounds(self):
        self._resource.isAbove = MagicMock(side_effect=lambda x: x == self._HEIGHT - 1)
        self.assertRaises(ValueError, self._env._addResource, self._resource)

    def test_resourceDistributor(self):
        self._env.addCell(self._cell)
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

    def test_cellLosesEnergyOfAction(self):

        cellAction = "left"
        self._cost[cellAction] = self._CELL_ENERGY / 2
        self._cost["right"] = 29

        self._cell.act = MagicMock(return_value=cellAction)
        self._env.addCell(self._cell)
        self._env.timeStep()
        self._cell.releaseEnergy.assert_called_with(self._cost[cellAction])

    def test_actionNotCompletedIfNotEnoughEnergy(self):

        cellAction = "left"
        self._cost[cellAction] = self._CELL_ENERGY + 10

        self._cell.act = MagicMock(return_value=cellAction)
        self._env.addCell(self._cell)
        self._env.timeStep()

        assert not self._cell.moveLeft.called

    def childHelper(self, cellCoords, childCoords, cellEnergyBefore, cellEnergyAfter, childEnergy):

        self._cost["reproduce"] = 0

        child = Cell()
        child.coordinates = MagicMock(return_value=childCoords)
        child.energy = MagicMock(return_value=childEnergy)

        self._cell.act = MagicMock(return_value="reproduce")
        self._cell.coordinates = MagicMock(return_value=cellCoords)
        self._cell.child = MagicMock(return_value=child)
        self._cell.energy = MagicMock(side_effect=
            lambda: cellEnergyBefore + int(self._cell.child.called) * (cellEnergyAfter - cellEnergyBefore))

        self._env.addCell(self._cell)

        return child

    def test_addsValidChildCell(self):
        child = self.childHelper(
            cellCoords=(9,2),
            childCoords=(9,2),
            cellEnergyBefore=16,
            cellEnergyAfter=8,
            childEnergy=6)
        self._env.timeStep()
        assert child in self._env.cells()

    def test_doesNotAddMovedChildCell(self):
        child = self.childHelper(
            cellCoords=(9,2),
            childCoords=(9,1),
            cellEnergyBefore=16,
            cellEnergyAfter=8,
            childEnergy=6)
        self._env.timeStep()
        assert child not in self._env.cells()

    def test_doesNotAddChildCellWithTooMuchEnergy(self):
        child = self.childHelper(
            cellCoords=(9,2),
            childCoords=(9,1),
            cellEnergyBefore=16,
            cellEnergyAfter=8,
            childEnergy=10)
        self._env.timeStep()
        assert child not in self._env.cells()

if __name__ == '__main__':
    unittest.main()
