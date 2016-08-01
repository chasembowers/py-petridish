import unittest

from mock import MagicMock

from petridish.cell import Cell
from petridish.environment import BasicEnvironment
from petridish.observer import Observer
from petridish.simulator import BasicSimulator
from petridish.update import Update
from petridish.update_factory import UpdateFactory


class TestBasicSimulator(unittest.TestCase):

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
        self.observer.observe = MagicMock(side_effect= \
            lambda env, loc: env if env is self.env and loc is self.CELL_LOCATION else None)

        self.simulator = BasicSimulator(self.env, self.observer, self.actions)

    def test_appliesUpdate(self):

        self.cell.act = MagicMock(side_effect=lambda env: self.ACTION_NAME if env is self.env else None)
        self.simulator.timeStep()
        self.update.apply.assert_called_with(self.env)



if __name__ == '__main__':
    unittest.main()