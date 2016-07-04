import unittest
from mock import MagicMock

from petridish.cell import Cell
from petridish.location import Location
from petridish.actor import Actor

class TestCell(unittest.TestCase):

    _X_EQUALS = 52
    _Y_EQUALS = 78

    def setUp(self):

        self._location = Location()
        self._actor = Actor()

        self._cell = Cell(self._location, self._actor)

        self._location.moveLeft = MagicMock()
        self._location.moveRight = MagicMock()
        self._location.moveUp = MagicMock()
        self._location.moveDown = MagicMock()
        self._location.isLeftOf = MagicMock()
        self._location.isRightOf = MagicMock()
        self._location.isBelow = MagicMock()
        self._location.isAbove = MagicMock()

        self._actor.act = MagicMock()

    def test_moveLeft(self):
        self._cell.moveLeft()
        self._location.moveLeft.assert_called_with()

    def test_moveRight(self):
        self._cell.moveRight()
        self._location.moveRight.assert_called_with()

    def test_moveUp(self):
        self._cell.moveUp()
        self._location.moveUp.assert_called_with()

    def test_moveDown(self):
        self._cell.moveDown()
        self._location.moveDown.assert_called_with()

    def test_isLeftOf(self):
        self._cell.isLeftOf(self._X_EQUALS)
        self._location.isLeftOf.assert_called_with(self._X_EQUALS)

    def test_isRightOf(self):
        self._cell.isRightOf(self._X_EQUALS)
        self._location.isRightOf.assert_called_with(self._X_EQUALS)

    def test_isBelow(self):
        self._cell.isBelow(self._Y_EQUALS)
        self._location.isBelow.assert_called_with(self._Y_EQUALS)

    def test_isAbove(self):
        self._cell.isAbove(self._Y_EQUALS)
        self._location.isAbove.assert_called_with(self._Y_EQUALS)

    def test_act(self):
        self._cell.act([])
        self._actor.act.assert_called_with([])

if __name__ == '__main__':
    unittest.main()
