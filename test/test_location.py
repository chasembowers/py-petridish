import unittest

from petridish.location import Location

class TestLocation(unittest.TestCase):

    def setUp(self):
        self._location = Location()

    def moveHelper(self, moveFunction, finalLoc):
        self.assertEqual(self._location.coordinates(), (0, 0))
        moveFunction()
        self.assertEqual(self._location.coordinates(), finalLoc)

    def doNothing(self): pass

    def test_noMove(self): self.moveHelper(self.doNothing, (0,0))

    def test_moveLeft(self): self.moveHelper(self._location.moveLeft, (-1,0))

    def test_moveRight(self): self.moveHelper(self._location.moveRight, (1,0))

    def test_moveUp(self): self.moveHelper(self._location.moveUp, (0,1))

    def test_moveDown(self): self.moveHelper(self._location.moveDown, (0,-1))

    def compareHelper(self, func, returnsTrue, returnsFalse):
        assert func(returnsTrue)
        assert not func(returnsFalse)

    def test_isBelow(self): self.compareHelper(self._location.isBelow, 1, 0)

    def test_isAbove(self): self.compareHelper(self._location.isAbove, -1, 0)

    def test_isLeftOf(self): self.compareHelper(self._location.isLeftOf, 1, 0)

    def test_isRightOf(self): self.compareHelper(self._location.isRightOf, -1, 0)

if __name__ == '__main__':
    unittest.main()
