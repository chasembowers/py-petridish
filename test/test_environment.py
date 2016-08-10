import unittest


from petridish.environment import RectangularEnvironment
from petridish.grid import FastGrid


class TestRectangularEnvironment(unittest.TestCase):

    WIDTH = 10
    HEIGHT = 20
    TYPE1 = 'type1'
    TYPE2 = 'type2'
    BODY1 = 'body1'
    BODY2 = 'body2'
    OUT_OF_BOUNDS = [(-1, HEIGHT / 2), (WIDTH, HEIGHT / 2), (WIDTH / 2, -1), (WIDTH / 2, HEIGHT)]

    def setUp(self):

        self.grid1 = FastGrid()
        self.grid2 = FastGrid()
        groups = {self.TYPE1: self.grid1, self.TYPE2: self.grid2}
        self.env = RectangularEnvironment(self.WIDTH, self.HEIGHT, groups)

    def test_insert(self):
        self.env.insert(self.TYPE1, self.BODY1, (5, 5))
        self.assertIn(self.BODY1, self.grid1)
        self.assertNotIn(self.BODY1, self.grid2)

    def test_mustInsertUniqueBody(self):
        self.env.insert(self.TYPE1, self.BODY1, (5, 5))
        self.assertRaises(ValueError, self.env.insert, self.TYPE2, self.BODY1, (5, 5))

    def test_locationMustBeTwoTuple(self):
        self.assertRaises(TypeError, self.env.insert, self.TYPE1, self.BODY1, (5, 5, 5))

    def test_cannotAddBodyOutOfBounds(self):
        for loc in self.OUT_OF_BOUNDS:
            self.assertRaises(ValueError, self.env.insert, self.TYPE1, self.BODY1, loc)

    def test_remove(self):
        self.env.insert(self.TYPE1, self.BODY1, (5, 5))
        self.env.remove(self.BODY1)
        self.assertNotIn(self.BODY1, self.grid1)

    def test_removeRaisesIfBodyDoesNotExist(self):
        self.assertRaises(LookupError, self.env.remove, self.BODY1)

    def test_locationOf(self):
        loc = (3,7)
        self.env.insert(self.TYPE1, self.BODY1, loc)
        self.assertEqual(self.env.locationOf(self.BODY1), loc)

    def test_locationOfRaisesIfBodyDoesNotExist(self):
        self.assertRaises(LookupError, self.env.locationOf, self.BODY1)

    def test_at(self):
        loc = (9,3)
        self.env.insert(self.TYPE1, self.BODY1, loc)
        self.assertEqual(self.env.at(loc, self.TYPE1), self.BODY1)

    def test_move(self):
        loc1 = (2,2)
        loc2 = (3,5)
        self.env.insert(self.TYPE1, self.BODY1, loc1)
        self.env.move(self.BODY1, loc2)
        self.assertEqual(self.env.locationOf(self.BODY1), loc2)

    def test_moveRaisesIfBodyDoesNotExist(self):
        self.assertRaises(LookupError, self.env.move, self.BODY1, (1,6))

    def test_inBounds(self):
        self.assertTrue(self.env.inBounds((self.WIDTH / 2, self.HEIGHT / 2)))
        for loc in self.OUT_OF_BOUNDS:
            self.assertFalse(self.env.inBounds(loc))

    def test_getItem(self):
        loc1 = (9, 3)
        loc2 = (7, 6)
        self.env.insert(self.TYPE1, self.BODY1, loc1)
        self.env.insert(self.TYPE2, self.BODY2, loc2)
        self.assertItemsEqual(self.env[self.TYPE1], [self.BODY1])
        self.assertItemsEqual(self.env[self.TYPE2], [self.BODY2])

    def test_width(self): self.assertEqual(self.env.width(), self.WIDTH)

    def test_height(self): self.assertEqual(self.env.height(), self.HEIGHT)

if __name__ == '__main__':
    unittest.main()