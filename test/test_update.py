import unittest

from petridish.energized import EnergyFactory, SimpleEnergy
from petridish.update import Move, BinaryResourceSpawner
from mock import MagicMock

from petridish.cell import Cell
from petridish.environment import RectangularEnvironment, Environment


class TestMoveUpdates(unittest.TestCase):

    WIDTH = 15
    HEIGHT = 25
    COST = 10

    CELL_LOCATION = (1, 2)
    CELL_X, CELL_Y = CELL_LOCATION
    UP = (0, 1)
    ABOVE = (CELL_X, CELL_Y + 1)
    DOWN = (0, -1)
    BELOW = (CELL_X, CELL_Y - 1)
    LEFT = (-1, 0)
    LEFT_OF = (CELL_X - 1, CELL_Y)
    RIGHT = (1, 0)
    RIGHT_OF = (CELL_X + 1, CELL_Y)

    def setUp(self):
        self.cell = Cell()
        self.cell.energy = MagicMock(return_value=self.COST + 10)
        self.cell.releaseEnergy = MagicMock()
        self.env = RectangularEnvironment(self.WIDTH, self.HEIGHT)

    def assertMoves(self, displacement, newLocation):
        self.env.insert('cells', self.cell, self.CELL_LOCATION)
        self.move = Move(self.CELL_LOCATION, displacement, self.COST)
        self.assertTrue(self.move.apply(self.env))
        self.assertEqual(self.env.locationOf(self.cell), newLocation)

    def test_movesUp(self): self.assertMoves(self.UP, self.ABOVE)

    def test_movesDown(self): self.assertMoves(self.DOWN, self.BELOW)

    def test_movesLeft(self): self.assertMoves(self.LEFT, self.LEFT_OF)

    def test_movesRight(self): self.assertMoves(self.RIGHT, self.RIGHT_OF)

    def test_cellLosesEnergy(self):
        self.env.insert('cells', self.cell, self.CELL_LOCATION)
        self.move = Move(self.CELL_LOCATION, self.UP, self.COST)
        self.move.apply(self.env)
        self.cell.releaseEnergy.assert_called_with(self.COST)

    def test_doesNotMoveIfNotEnoughEnergy(self):
        self.env.insert('cells', self.cell, self.CELL_LOCATION)
        self.move = Move(self.CELL_LOCATION, self.UP, self.COST)
        self.cell.energy = MagicMock(return_value=self.COST / 2.)

    def test_doesNotMoveIfOccupied(self):
        self.env.insert('cells', self.cell, self.CELL_LOCATION)
        self.move = Move(self.CELL_LOCATION, self.UP, self.COST)
        self.env.insert('cells', Cell(), self.ABOVE)
        self.assertFalse(self.move.apply(self.env))
        self.assertEqual(self.env.locationOf(self.cell), self.CELL_LOCATION)

    def test_doesNotMoveIfOutOfBounds(self):
        CORNER = (0,0)
        self.env.insert('cells', self.cell, CORNER)
        self.move = Move(CORNER, self.LEFT, self.COST)
        self.assertFalse(self.move.apply(self.env))
        self.assertEqual(self.env.locationOf(self.cell), CORNER)

    def test_cannotMoveUnplacedCell(self):
        self.env.insert('cells', self.cell, self.CELL_LOCATION)
        self.move = Move(self.BELOW, self.UP, self.COST)
        self.assertFalse(self.move.apply(self.env))

class TestBinaryResourceSpawner(unittest.TestCase):

    WIDTH = 15
    HEIGHT = 25
    ENERGY = 9
    RESOURCE_LOCATION = (4,8)

    def setUp(self):

        self.resource = SimpleEnergy(self.ENERGY)
        self.factory = EnergyFactory()
        self.factory.produce = MagicMock(return_value=self.resource)

        self.spawner = BinaryResourceSpawner(1, self.factory)

        self.env = RectangularEnvironment(self.WIDTH, self.HEIGHT)
        self.env.randomLocation = MagicMock(return_value=self.RESOURCE_LOCATION)

    def test_spawnsResource(self):
        self.spawner.apply(self.env)
        self.assertEqual(self.env.locationOf(self.resource), self.RESOURCE_LOCATION)
        self.assertEqual(len(set(self.env['resources'])), 1)

    def test_doesNotSpawnIfLocationOccupied(self):
        self.env.insert('resources', SimpleEnergy(self.ENERGY), self.RESOURCE_LOCATION)
        self.spawner.apply(self.env)
        self.assertFalse(self.resource in self.env['resources'])
        self.assertEqual(len(set(self.env['resources'])), 1)

if __name__ == '__main__':
    unittest.main()