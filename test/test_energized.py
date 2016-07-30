import unittest

from petridish.energized import SimpleEnergy

class TestSimpleEnergy(unittest.TestCase):

    INITIAL_ENERGY = 51
    CHILD_ENERGY_RATIO = .34

    def setUp(self):
        self._simpleEnergy = SimpleEnergy(self.INITIAL_ENERGY, self.CHILD_ENERGY_RATIO)

    def test_consumeSomeEnergy(self):
        someEnergy = 37
        self._simpleEnergy.consumeEnergy(someEnergy)
        energyAfter = self._simpleEnergy.energy()
        self.assertEqual(energyAfter - self.INITIAL_ENERGY, someEnergy)

    def test_consumeNegativeEnergy(self):
        negativeEnergy = -94
        self.assertRaises(ValueError, self._simpleEnergy.consumeEnergy, negativeEnergy)

    def test_releaseSomeEnergy(self):
        someEnergy = 34
        self._simpleEnergy.releaseEnergy(someEnergy)
        self.assertEqual(self._simpleEnergy.energy(), self.INITIAL_ENERGY - someEnergy)

    def test_releaseTooMuchEnergy(self):
        tooMuchEnergy = self.INITIAL_ENERGY + 10
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
        self.assertEqual(self._simpleEnergy.energy(), initialEnergy * (1 - self.CHILD_ENERGY_RATIO))
        self.assertEqual(child.energy(), initialEnergy * self.CHILD_ENERGY_RATIO)
        self.assertNotEqual(self._simpleEnergy, child)

if __name__ == '__main__':
    unittest.main()