import unittest

from petridish.grid import FastGrid


class TestFastGrid(unittest.TestCase):

    WIDTH = 10
    HEIGHT = 20

    def setUp(self):
        self.grid = FastGrid(self.WIDTH, self.HEIGHT)

    def test_widthAndHeight(self):
        self.assertEqual(self.grid.width(), self.WIDTH)
        self.assertEqual(self.grid.height(), self.HEIGHT)

    def test_addBody(self):
        body = 'body'
        location = (1,2)
        self.grid.insert(body, location)
        self.assertIn(body, self.grid)
        self.assertEqual(self.grid.locationOf(body), location)
        self.assertEqual(self.grid.at(location), body)

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

    def test_NoBodyAtUnoccupiedLocation(self):
        self.assertEqual(self.grid.at((1, 2)), None)

    def test_removeBody(self):
        body = 'body'
        location = (1, 2)
        self.grid.insert(body, location)
        self.grid.remove(body)
        self.assertNotIn(body, self.grid)
        self.assertEqual(self.grid.at(location), None)
        self.assertRaises(LookupError, self.grid.locationOf, body)

    def test_cannotRemoveUnplacedBody(self):
        self.assertRaises(LookupError, self.grid.remove, 'body')

    def test_removeAtLocation(self):
        body = 'body'
        location = (1, 2)
        self.grid.insert(body, location)
        self.grid.removeAt(location)
        self.assertNotIn(body, self.grid)

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
        self.assertEqual(self.grid.locationOf(body), newLocation)

    def test_length(self):
        bodies = ['body1', 'body2']
        for i in range(len(bodies)):
            self.grid.insert(bodies[i], (0, i))
        self.assertEqual(len(self.grid), len(bodies))

    def test_iteration(self):
        bodies = ['body1', 'body2', 'body3']
        for i in range(len(bodies)):
            self.grid.insert(bodies[i], (0, i))
        self.assertEqual(set(self.grid), set(bodies))

if __name__ == '__main__':
    unittest.main()
