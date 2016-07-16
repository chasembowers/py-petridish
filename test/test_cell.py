import unittest
from mock import MagicMock

from petridish.cell import BasicCell, Cell
from petridish.energized import Energized
from petridish.point import Point
from petridish.actor import Actor
from petridish.resource import Resource


class TestBasicCell(unittest.TestCase):

    _X_EQUALS = 52
    _Y_EQUALS = 78

    def setUp(self):

        self._location = Point()
        self._actor = Actor()
        self._energized = Energized()

        self._cell = BasicCell(self._actor, self._energized, self._location)

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

        self._energized.consumeEnergy = MagicMock()
        self._energized.releaseEnergy = MagicMock()
        self._energized.energy = MagicMock(return_value=23)

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
        cells = [self._cell, Cell(), Cell()]
        resources = [Resource()]
        self._cell.act(cells, resources)
        self._actor.act.assert_called_with(self._cell, cells, resources)

    def test_consumeSomeEnergy(self):
        someEnergy = 37
        self._cell.consumeEnergy(someEnergy)
        self._energized.consumeEnergy.assert_called_with(someEnergy)

    def test_releaseSomeEnergy(self):
        someEnergy = 34
        self._cell.releaseEnergy(someEnergy)
        self._energized.releaseEnergy.assert_called_with(someEnergy)

    def test_getEnergy(self):
        assert self._cell.energy() == self._energized.energy()
        self._energized.energy.assert_called_with()

if __name__ == '__main__':
    unittest.main()
