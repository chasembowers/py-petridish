import unittest

from petridish.update_factory import MoveFactory
from petridish.update import Move


class TestMoveFactory(unittest.TestCase):

    DISPLACEMENT = (0,1)
    COST = 15

    def setUp(self):
        self.factory = MoveFactory(self.DISPLACEMENT, self.COST)

    def test_producesCorrectMoveA(self):
        cellLocation = (1,5)
        self.assertEqual(self.factory.produce(cellLocation), Move(cellLocation, self.DISPLACEMENT, self.COST))

    def test_producesCorrectMoveB(self):
        cellLocation = (4,2)
        self.assertEqual(self.factory.produce(cellLocation), Move(cellLocation, self.DISPLACEMENT, self.COST))

if __name__ == '__main__':
    unittest.main()
