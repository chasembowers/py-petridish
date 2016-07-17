import unittest
from mock import MagicMock

from petridish.cell import BasicCell, Cell
from petridish.energized import Energized
from petridish.point import Point
from petridish.actor import Actor, RandomActor
from petridish.resource import Resource


class TestRandomActor(unittest.TestCase):

    def setUp(self):

        self._randomActor = RandomActor()

    def test_act(self):

        assert self._randomActor.act(None, None, None) in ['left', 'right', 'up', 'down', '']

    def test_child(self):

        assert type(self._randomActor.child()) == type(self._randomActor)

if __name__ == '__main__':
    unittest.main()
