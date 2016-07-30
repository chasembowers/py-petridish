import unittest

from petridish.action import Move
from mock import MagicMock

from petridish.cell import Cell
from petridish.environment import BasicEnvironment


class TestMoveActions(unittest.TestCase):

    WIDTH = 15
    HEIGHT = 25
    COST = 10

    CELL_LOCATION = (1, 2)
    CELL_X, CELL_Y = CELL_LOCATION
    UP = 'up'
    ABOVE = (CELL_X, CELL_Y + 1)
    DOWN = 'down'
    BELOW = (CELL_X, CELL_Y - 1)
    LEFT = 'left'
    LEFT_OF = (CELL_X - 1, CELL_Y)
    RIGHT = 'right'
    RIGHT_OF = (CELL_X + 1, CELL_Y)

    def setUp(self):
        self.cell = Cell()
        self.cell.energy = MagicMock(return_value=self.COST + 10)
        self.cell.releaseEnergy = MagicMock()
        self.env = BasicEnvironment(self.WIDTH, self.HEIGHT)
        self.move = Move(self.COST)
        self.env.cells.insert(self.cell, self.CELL_LOCATION)

    def assertMoves(self, cellArgs, newLocation):
        self.assertTrue(self.move.apply(self.env, self.CELL_LOCATION, cellArgs))
        self.assertEqual(self.env.cells.locationOf(self.cell), newLocation)

    def test_movesUp(self): self.assertMoves(self.UP, self.ABOVE)

    def test_movesDown(self): self.assertMoves(self.DOWN, self.BELOW)

    def test_movesLeft(self): self.assertMoves(self.LEFT, self.LEFT_OF)

    def test_movesRight(self): self.assertMoves(self.RIGHT, self.RIGHT_OF)

    def test_cellLosesEnergy(self):
        self.move.apply(self.env, self.CELL_LOCATION, self.UP)
        self.cell.releaseEnergy.assert_called_with(self.COST)

    def test_doesNotMoveIfNotEnoughEnergy(self):
        self.cell.energy = MagicMock(return_value=self.COST / 2.)
        self.assertFalse(self.move.apply(self.env, self.CELL_LOCATION, self.UP))

    def test_doesNotMoveIfOccupied(self):
        self.env.cells.insert(Cell(), self.ABOVE)
        self.assertFalse(self.move.apply(self.env, self.CELL_LOCATION, self.UP))
        self.assertEqual(self.env.cells.locationOf(self.cell), self.CELL_LOCATION)

    def test_cannotMoveUnplacedCell(self):
        self.assertFalse(self.move.apply(self.env, self.BELOW, self.UP))


if __name__ == '__main__':
    unittest.main()