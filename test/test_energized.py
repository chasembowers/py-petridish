import unittest

from petridish.energized import SimpleEnergy

class TestSimpleEnergy(unittest.TestCase):

    _initialEnergy = 51
    _childEnergyRatio = .34

    def setUp(self):
        self._simpleEnergy = SimpleEnergy(self._initialEnergy, self._childEnergyRatio)

    def test_consumeSomeEnergy(self):
        someEnergy = 37
        self._simpleEnergy.consumeEnergy(someEnergy)
        energyAfter = self._simpleEnergy.energy()
        assert energyAfter - self._initialEnergy == someEnergy

    def test_consumeNegativeEnergy(self):
        negativeEnergy = -94
        self.assertRaises(ValueError, self._simpleEnergy.consumeEnergy, negativeEnergy)

    def test_releaseSomeEnergy(self):
        someEnergy = 34
        self._simpleEnergy.releaseEnergy(someEnergy)
        assert self._simpleEnergy.energy() == self._initialEnergy - someEnergy

    def test_releaseTooMuchEnergy(self):
        tooMuchEnergy = self._initialEnergy + 10
        self.assertRaises(ValueError, self._simpleEnergy.releaseEnergy, tooMuchEnergy)

    def test_releaseNegativeEnergy(self):
        negativeEnergy = -32
        self.assertRaises(ValueError, self._simpleEnergy.releaseEnergy, negativeEnergy)

    def test_negativeInitialEnergy(self):
        self.assertRaises(ValueError, self._simpleEnergy.__init__, -5)

    def test_negativeChildEnergyRatio(self):
        self.assertRaises(ValueError, self._simpleEnergy.__init__, 10, -.2)

    def test_ChildEnergyRatioLargerThanOne(self):
        self.assertRaises(ValueError, self._simpleEnergy.__init__, 10, 1.1)

    def test_createChild(self):
        initialEnergy = self._simpleEnergy.energy()
        child = self._simpleEnergy.child()
        assert self._simpleEnergy.energy() == initialEnergy * (1 - self._childEnergyRatio)
        print child.energy()
        print initialEnergy
        print self._childEnergyRatio
        assert child.energy() == initialEnergy * self._childEnergyRatio
        assert self._simpleEnergy != child

if __name__ == '__main__':
    unittest.main()
