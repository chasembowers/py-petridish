import unittest
from mock import MagicMock

from petridish.point import Point
from petridish.resource import BasicResource


class TestBasicResource(unittest.TestCase):

    _ENERGY = 48
    _SOME_ENERGY = 34
    _TOO_MUCH_ENERGY = 67
    _NEGATIVE_ENERGY = -32

    _X_EQUALS = 98
    _Y_EQUALS = 28

    def setUp(self):

        self._location = Point()
        self._resource = BasicResource(self._ENERGY, self._location)

        self._location.isLeftOf = MagicMock()
        self._location.isRightOf = MagicMock()
        self._location.isBelow = MagicMock()
        self._location.isAbove = MagicMock()

    def test_isLeftOf(self):
        self._resource.isLeftOf(self._X_EQUALS)
        self._location.isLeftOf.assert_called_with(self._X_EQUALS)

    def test_isRightOf(self):
        self._resource.isRightOf(self._X_EQUALS)
        self._location.isRightOf.assert_called_with(self._X_EQUALS)

    def test_isBelow(self):
        self._resource.isBelow(self._Y_EQUALS)
        self._location.isBelow.assert_called_with(self._Y_EQUALS)

    def test_isAbove(self):
        self._resource.isAbove(self._Y_EQUALS)
        self._location.isAbove.assert_called_with(self._Y_EQUALS)

    def test_giveSomeEnergy(self):
        self._resource.giveEnergy(self._SOME_ENERGY)
        assert self._resource.energy() == self._ENERGY - self._SOME_ENERGY

    def test_giveTooMuchEnergy(self):
        self.assertRaises(ValueError, self._resource.giveEnergy, self._TOO_MUCH_ENERGY)

    def test_giveNegativeEnergy(self):
        self.assertRaises(ValueError, self._resource.giveEnergy, self._NEGATIVE_ENERGY)

if __name__ == '__main__':
    unittest.main()
