import unittest

from mock import MagicMock, call

from petridish.cell import Cell
from petridish.environment import RectangularEnvironment
from petridish.observe import Observer, Observations
from petridish.simulator import RandomOrderSimulator
from petridish.update import Update
from petridish.update_factory import UpdateFactory


class TestRandomOrderSimulator(unittest.TestCase):

    CELL1_LOCATION = (4, 5)
    CELL2_LOCATION = (7, 9)
    WIDTH = 25
    HEIGHT = 42
    ACTION_NAME = 'act'

    def setUp(self):

        self.stepUpdate1 = Update()
        self.stepUpdate1.apply = MagicMock()
        self.stepUpdate2 = Update()
        self.stepUpdate2.apply = MagicMock()
        self.stepUpdates = [self.stepUpdate1, self.stepUpdate2]

        self.cell1 = Cell()
        self.cell2 = Cell()

        self.env = RectangularEnvironment(self.WIDTH, self.HEIGHT)
        self.env.insert('cells', self.cell1, self.CELL1_LOCATION)
        self.env.insert('cells', self.cell2, self.CELL2_LOCATION)

        self.actionUpdate = Update()
        self.actionUpdate.apply = MagicMock()

        self.factory = UpdateFactory()
        self.factory.produce = MagicMock(side_effect= \
            lambda loc: self.actionUpdate if loc is self.CELL1_LOCATION or self.CELL2_LOCATION else None)

        self.actions = {self.ACTION_NAME: self.factory}

        self.observations = Observations()
        self.observer = Observer()
        self.observer.observe = MagicMock(side_effect=lambda env: self.observations if env is self.env else None)

        self.cell1.act = MagicMock(side_effect= \
            lambda obs, loc: self.ACTION_NAME if obs is self.observations and loc is self.CELL1_LOCATION else None)
        self.cell2.act = MagicMock(side_effect= \
            lambda obs, loc: self.ACTION_NAME if obs is self.observations and loc is self.CELL2_LOCATION else None)

        self.simulator = RandomOrderSimulator(self.env, self.observer, self.actions, self.stepUpdates)

    def test_appliesActionUpdates(self):

        self.simulator.timeStep()
        self.assertEqual(self.actionUpdate.apply.mock_calls, [call(self.env), call(self.env)])

    def test_appliesStepUpdates(self):

        self.simulator.timeStep()
        self.stepUpdate1.apply.assert_called_with(self.env)
        self.stepUpdate2.apply.assert_called_with(self.env)

    def test_getEnvironment(self):
        self.assertEqual(self.simulator.environment(), self.env)


if __name__ == '__main__':
    unittest.main()
