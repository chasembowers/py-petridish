import unittest

from petridish.point import Point

class TestPoint(unittest.TestCase):

    def setUp(self):
        self._point = Point()

    def moveHelper(self, moveFunction, finalLoc):
        self.assertEqual(self._point.coordinates(), (0, 0))
        moveFunction()
        self.assertEqual(self._point.coordinates(), finalLoc)

    def doNothing(self): pass

    def test_noMove(self): self.moveHelper(self.doNothing, (0,0))

    def test_moveLeft(self): self.moveHelper(self._point.moveLeft, (-1, 0))

    def test_moveRight(self): self.moveHelper(self._point.moveRight, (1, 0))

    def test_moveUp(self): self.moveHelper(self._point.moveUp, (0, 1))

    def test_moveDown(self): self.moveHelper(self._point.moveDown, (0, -1))

    def compareHelper(self, func, returnsTrue, returnsFalse):
        assert func(returnsTrue)
        assert not func(returnsFalse)

    def test_isBelow(self): self.compareHelper(self._point.isBelow, 1, 0)

    def test_isAbove(self): self.compareHelper(self._point.isAbove, -1, 0)

    def test_isLeftOf(self): self.compareHelper(self._point.isLeftOf, 1, 0)

    def test_isRightOf(self): self.compareHelper(self._point.isRightOf, -1, 0)

    def test_moveTo(self):
        coordinates = (2,8)
        self._point.moveTo(coordinates)
        assert self._point.coordinates() == coordinates

if __name__ == '__main__':
    unittest.main()
