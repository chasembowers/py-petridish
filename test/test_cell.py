import unittest
from mock import MagicMock

from petridish.cell import BasicCell
from petridish.energized import Energized
from petridish.actor import Actor

from petridish.introspector import Introspector
from petridish.observations import Observations


class TestBasicCell(unittest.TestCase):

    def setUp(self):

        self.actor = Actor()
        self.introspector = Introspector()
        self.energized = Energized()

        self.cell = BasicCell(self.actor, self.energized, self.introspector)

    def test_act(self):
        observations = Observations()
        cellLocation = (8,3)
        self.introspector.introspect = MagicMock(side_effect=lambda cell: cell)

        action = 'act'
        self.actor.act = MagicMock(side_effect= \
            lambda cell, obs, loc: action if cell is self.cell and obs is observations and loc is cellLocation else None)

        self.assertEqual(self.cell.act(observations, cellLocation), action)

    def test_consumeSomeEnergy(self):
        self.energized.consumeEnergy = MagicMock()
        someEnergy = 37
        self.cell.consumeEnergy(someEnergy)
        self.energized.consumeEnergy.assert_called_with(someEnergy)

    def test_releaseSomeEnergy(self):
        self.energized.releaseEnergy = MagicMock()
        someEnergy = 34
        self.cell.releaseEnergy(someEnergy)
        self.energized.releaseEnergy.assert_called_with(someEnergy)

    def test_getEnergy(self):
        self.energized.energy = MagicMock(return_value=23)
        self.assertEqual(self.cell.energy(), self.energized.energy())

    def test_equality(self):
        self.assertEqual(self.cell, BasicCell(self.actor, self.energized, self.introspector))

    def test_producesChild(self):
        childActor = Actor()
        childEnergized = Energized()

        self.actor.child = MagicMock(return_value=childActor)
        self.energized.child = MagicMock(return_value=childEnergized)

        child = self.cell.child()
        self.assertNotEqual(child, self.cell)
        self.assertEqual(child, BasicCell(childActor, childEnergized, self.introspector))

if __name__ == '__main__':
    unittest.main()