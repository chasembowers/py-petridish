import unittest
from mock import MagicMock

from petridish.cell import BasicCell
from petridish.point import Point
from petridish.actor import Actor
from petridish.resource import Resource


class TestBasicCell(unittest.TestCase):

    _X_EQUALS = 52
    _Y_EQUALS = 78
    _CELL_ENERGY = 47

    def setUp(self):

        self._location = Point()
        self._actor = Actor()

        self._cell = BasicCell(self._actor, self._CELL_ENERGY, self._location)

        self._location.moveLeft = MagicMock()
        self._location.moveRight = MagicMock()
        self._location.moveUp = MagicMock()
        self._location.moveDown = MagicMock()
        self._location.moveTo = MagicMock()
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

    def test_moveTo(self):
        coordinates = (8,7)
        self._cell.moveTo(coordinates)
        self._location.moveTo.assert_called_with(coordinates)

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

    def test_consumeSomeEnergy(self):
        someEnergy = 37
        self._cell.consumeEnergy(someEnergy)
        cellEnergyAfter = self._cell.energy()
        assert cellEnergyAfter - self._CELL_ENERGY == someEnergy

    def test_consumeNegativeEnergy(self):
        negativeEnergy = -94
        self.assertRaises(ValueError, self._cell.consumeEnergy, negativeEnergy)

if __name__ == '__main__':
    unittest.main()
