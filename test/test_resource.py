import unittest
from mock import MagicMock

from petridish.energized import Energized
from petridish.point import Point
from petridish.resource import BasicResource


class TestBasicResource(unittest.TestCase):

    _X_EQUALS = 98
    _Y_EQUALS = 28

    def setUp(self):

        self._location = Point()
        self._energized = Energized()
        self._resource = BasicResource(self._energized, self._location)

        self._location.isLeftOf = MagicMock()
        self._location.isRightOf = MagicMock()
        self._location.isBelow = MagicMock()
        self._location.isAbove = MagicMock()

        self._energized.consumeEnergy = MagicMock()
        self._energized.releaseEnergy = MagicMock()
        self._energized.energy = MagicMock(return_value=92)

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

    def test_releaseSomeEnergy(self):
        someEnergy = 34
        self._resource.releaseEnergy(someEnergy)
        self._energized.releaseEnergy.assert_called_with(someEnergy)

    def test_getEnergy(self):
        assert self._resource.energy() == self._energized.energy()
        self._energized.energy.assert_called_with()

if __name__ == '__main__':
    unittest.main()
