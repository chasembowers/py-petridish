import unittest
from petridish.actor import RandomActor


class TestRandomActor(unittest.TestCase):

    def setUp(self):

        self._randomActor = RandomActor()

    def test_returnsValidAction(self):

        assert self._randomActor.act(None, None, None) in ['left', 'right', 'up', 'down', '']

    def test_producesChild(self):

        assert type(self._randomActor.child()) == type(self._randomActor)

if __name__ == '__main__':
    unittest.main()
