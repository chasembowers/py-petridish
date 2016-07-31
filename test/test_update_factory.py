import unittest

from petridish.update_factory import MoveFactory
from petridish.update import Move


class TestMoveFactory(unittest.TestCase):

    COST = 15

    def setUp(self):
        self.factory = MoveFactory(self.COST)

    def test_producesCorrectMoveA(self):
        cellLocation = (1,5)
        direction = 'up'
        self.assertEqual(self.factory.produce(cellLocation, direction), Move(cellLocation, direction, self.COST))

    def test_producesCorrectMoveB(self):
        cellLocation = (4,2)
        direction = 'left'
        self.assertEqual(self.factory.produce(cellLocation, direction), Move(cellLocation, direction, self.COST))

if __name__ == '__main__':
    unittest.main()
