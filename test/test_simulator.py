import unittest

from mock import MagicMock

from petridish.cell import Cell
from petridish.environment import BasicEnvironment
from petridish.observer import Observer
from petridish.simulator import RandomOrderSimulator
from petridish.update import Update
from petridish.update_factory import UpdateFactory


class TestRandomOrderSimulator(unittest.TestCase):

    CELL_LOCATION = (4,5)
    WIDTH = 25
    HEIGHT = 42
    ACTION_NAME = 'act'

    def setUp(self):

        self.cell = Cell()

        self.env = BasicEnvironment(self.WIDTH, self.HEIGHT)
        self.env.cells.insert(self.cell, self.CELL_LOCATION)

        self.update = Update()
        self.update.apply = MagicMock()

        self.factory = UpdateFactory()
        self.factory.produce = MagicMock(side_effect=lambda loc: self.update if loc is self.CELL_LOCATION else None)

        self.actions = {self.ACTION_NAME: self.factory}

        self.observer = Observer()
        self.observer.observe = MagicMock(side_effect=lambda env: env)

        self.simulator = RandomOrderSimulator(self.env, self.observer, self.actions)

    def test_appliesUpdate(self):

        self.cell.act = MagicMock(side_effect= \
            lambda obs, loc: self.ACTION_NAME if obs is self.env and loc is self.CELL_LOCATION else None)
        self.simulator.timeStep()
        self.update.apply.assert_called_with(self.env)



if __name__ == '__main__':
    unittest.main()