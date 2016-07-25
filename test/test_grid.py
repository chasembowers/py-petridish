import unittest

from petridish.grid import FastGrid


class TestFastGrid(unittest.TestCase):

    _WIDTH = 10
    _HEIGHT = 20

    def setUp(self):
        self.grid = FastGrid(self._WIDTH, self._HEIGHT)

    def test_widthAndHeight(self):
        assert self.grid.width() == self._WIDTH
        assert self.grid.height() == self._HEIGHT

    def test_addBody(self):
        body = 'body'
        location = (1,2)
        self.grid.insert(body, location)
        assert body in self.grid
        assert self.grid.locationOf(body) is location
        assert self.grid.at(location) is body

    def test_cannotAddBodyTwice(self):
        body = 'body'
        self.grid.insert(body, (1, 2))
        self.assertRaises(ValueError, self.grid.insert, body, (3, 4))

    def test_cannotAddTwoBodiesToSameLocation(self):
        location = (1, 2)
        self.grid.insert('a', location)
        self.assertRaises(ValueError, self.grid.insert, 'b', location)

    def test_cannotGetLocationOfUnplacedBody(self):
        self.assertRaises(LookupError, self.grid.locationOf, 'a')

    def test_cannotGetBodyAtUnoccupiedLocation(self):
        self.assertRaises(LookupError, self.grid.at, (1, 2))

    def test_removeBody(self):
        body = 'body'
        location = (1, 2)
        self.grid.insert(body, location)
        self.grid.remove(body)
        assert body not in self.grid
        self.assertRaises(LookupError, self.grid.at, location)
        self.assertRaises(LookupError, self.grid.locationOf, body)

    def test_cannotRemoveUnplacedBody(self):
        self.assertRaises(LookupError, self.grid.remove, 'body')

    def test_removeAtLocation(self):
        body = 'body'
        location = (1, 2)
        self.grid.insert(body, location)
        self.grid.removeAt(location)
        assert body not in self.grid

    def test_cannotRemoveAtUnoccupiedLocation(self):
        self.assertRaises(LookupError, self.grid.removeAt, (1, 2))

    def test_locationMustBeTwoTuple(self):
        self.assertRaises(TypeError, self.grid.insert, 'body', (1, 2, 3))

    def test_cannotAddBodyOutOfBounds(self):
        body = 'body'
        self.assertRaises(ValueError, self.grid.insert, body, (-1, 10))
        self.assertRaises(ValueError, self.grid.insert, body, (10, 10))
        self.assertRaises(ValueError, self.grid.insert, body, (5, -1))
        self.assertRaises(ValueError, self.grid.insert, body, (5, 20))

    def test_moveBody(self):
        body = 'body'
        newLocation = (3,4)
        self.grid.insert(body, (1, 2))
        self.grid.move(body, newLocation)
        assert self.grid.locationOf(body) is newLocation

if __name__ == '__main__':
    unittest.main()