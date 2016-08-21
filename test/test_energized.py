import unittest

from petridish.energized import SimpleEnergy, SimpleEnergyOrgan

class TestSimpleEnergy(unittest.TestCase):

    INITIAL_ENERGY = 51

    def setUp(self):
        self.energy = SimpleEnergy(self.INITIAL_ENERGY)

    def test_consumeSomeEnergy(self):
        someEnergy = 37
        self.energy.consumeEnergy(someEnergy)
        energyAfter = self.energy.energy()
        self.assertEqual(energyAfter - self.INITIAL_ENERGY, someEnergy)

    def test_consumeNegativeEnergy(self):
        negativeEnergy = -94
        self.assertRaises(ValueError, self.energy.consumeEnergy, negativeEnergy)

    def test_releaseSomeEnergy(self):
        someEnergy = 34
        self.energy.releaseEnergy(someEnergy)
        self.assertEqual(self.energy.energy(), self.INITIAL_ENERGY - someEnergy)

    def test_releaseTooMuchEnergy(self):
        tooMuchEnergy = self.INITIAL_ENERGY + 10
        self.assertRaises(ValueError, self.energy.releaseEnergy, tooMuchEnergy)

    def test_releaseNegativeEnergy(self):
        negativeEnergy = -32
        self.assertRaises(ValueError, self.energy.releaseEnergy, negativeEnergy)

    def test_negativeInitialEnergy(self):
        self.assertRaises(ValueError, self.energy.__init__, -5)


class TestSimpleEnergyOrgan(unittest.TestCase):

    INITIAL_ENERGY = 37
    CHILD_ENERGY_RATIO = .34

    def setUp(self):
        self.organ = SimpleEnergyOrgan(self.INITIAL_ENERGY, self.CHILD_ENERGY_RATIO)

    def test_negativeChildEnergyRatio(self):
        self.assertRaises(ValueError, self.organ.__init__, 10, -.2)

    def test_ChildEnergyRatioLargerThanOne(self):
        self.assertRaises(ValueError, self.organ.__init__, 10, 1.1)

    def test_createChild(self):
        initialEnergy = self.organ.energy()
        child = self.organ.child()
        childEnergy = initialEnergy * self.CHILD_ENERGY_RATIO
        self.assertEqual(self.organ.energy(), initialEnergy - childEnergy)
        self.assertEqual(child.energy(), childEnergy)
        self.assertNotEqual(self.organ, child)

if __name__ == '__main__':
    unittest.main()