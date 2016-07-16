import unittest

from petridish.energized import SimpleEnergy

class TestSimpleEnergy(unittest.TestCase):

    _initialEnergy = 51

    def setUp(self):
        self._energy = SimpleEnergy(self._initialEnergy)

    def test_consumeSomeEnergy(self):
        someEnergy = 37
        self._energy.consumeEnergy(someEnergy)
        energyAfter = self._energy.energy()
        assert energyAfter - self._initialEnergy == someEnergy

    def test_consumeNegativeEnergy(self):
        negativeEnergy = -94
        self.assertRaises(ValueError, self._energy.consumeEnergy, negativeEnergy)

    def test_releaseSomeEnergy(self):
        someEnergy = 34
        self._energy.releaseEnergy(someEnergy)
        assert self._energy.energy() == self._initialEnergy - someEnergy

    def test_releaseTooMuchEnergy(self):
        tooMuchEnergy = self._initialEnergy + 10
        self.assertRaises(ValueError, self._energy.releaseEnergy, tooMuchEnergy)

    def test_releaseNegativeEnergy(self):
        negativeEnergy = -32
        self.assertRaises(ValueError, self._energy.releaseEnergy, negativeEnergy)


if __name__ == '__main__':
    unittest.main()
