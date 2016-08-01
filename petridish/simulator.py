import random

from petridish.update_factory import MoveFactory


class BasicSimulator:

    def __init__(self, environment, observer, actions=None):

        self._env = environment
        self._observer = observer

        if not actions:
            actions = {
                'up': MoveFactory((0, 1), 10),
                'down': MoveFactory((0, -1), 10),
                'left': MoveFactory((-1, 0), 10),
                'right': MoveFactory((1, 0), 10)
            }
        self._actions = actions

    def timeStep(self):

        for cell in random.sample(self._env.cells, len(self._env.cells)):
            cellLocation = self._env.cells.locationOf(cell)
            observations = self._observer.observe(self._env, cellLocation)
            action = cell.act(observations)
            updateFactory = self._actions[action]
            update = updateFactory.produce(cellLocation)
            update.apply(self._env)