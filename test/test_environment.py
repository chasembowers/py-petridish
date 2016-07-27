import unittest

from petridish.environment import BasicEnvironment


class TestBasicEnvironment(unittest.TestCase):

    WIDTH = 10
    HEIGHT = 20

    def setUp(self):
        self.env = BasicEnvironment(self.WIDTH, self.HEIGHT)

    def test_createsGridsWithWidthAndHeight(self):
        assert self.env.cells.width() == self.WIDTH
        assert self.env.cells.height() == self.HEIGHT
        assert self.env.resources.width() == self.WIDTH
        assert self.env.resources.height() == self.HEIGHT

if __name__ == '__main__':
    unittest.main()