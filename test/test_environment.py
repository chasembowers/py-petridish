import unittest

from petridish.environment import BasicEnvironment


class TestBasicEnvironment(unittest.TestCase):

    _WIDTH = 10
    _HEIGHT = 20

    def setUp(self):
        self.env = BasicEnvironment(self._WIDTH, self._HEIGHT)

    def test_createsGridsWithWidthAndHeight(self):
        assert self.env.cells.width() == self._WIDTH
        assert self.env.cells.height() == self._HEIGHT
        assert self.env.resources.width() == self._WIDTH
        assert self.env.resources.height() == self._HEIGHT

if __name__ == '__main__':
    unittest.main()