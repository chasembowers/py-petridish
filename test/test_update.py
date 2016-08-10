import unittest

from petridish.update import Move
from mock import MagicMock

from petridish.cell import Cell
from petridish.environment import RectangularEnvironment


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


if __name__ == '__main__':
    unittest.main()