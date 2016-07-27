import unittest

from petridish.action import MoveUp
from mock import MagicMock

from petridish.environment import BasicEnvironment


class TestMoveActions(unittest.TestCase):

    WIDTH = 15
    HEIGHT = 25
    COST = 10
    CELL_LOCATION = (1, 2)
    ABOVE = (CELL_LOCATION[0], CELL_LOCATION[1] + 1)

    def setUp(self):
        self.cell = 'cell'
        self.env = BasicEnvironment(self.WIDTH, self.HEIGHT)
        self.moveUp = MoveUp(self.COST)
        self.env.cells.insert(self.cell, self.CELL_LOCATION)

    def test_cost(self):
        assert self.moveUp.cost() == self.COST

    def test_moveUp(self):
        assert self.moveUp.apply(self.cell, self.env) == True
        assert self.env.cells.locationOf(self.cell) == self.ABOVE

    def test_doesNotMoveUpIfOccupied(self):
        self.env.cells.insert('other', self.ABOVE)
        assert self.moveUp.apply(self.cell, self.env) == False
        assert self.env.cells.locationOf(self.cell) == self.CELL_LOCATION

    def test_cannotMoveUnplacedCell(self):
        assert self.moveUp.apply('unplaced', self.env) == False


    #point to cell st existence is guaranteed


if __name__ == '__main__':
    unittest.main()