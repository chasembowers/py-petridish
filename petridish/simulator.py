import random

from petridish.update_factory import MoveFactory


class RandomOrderSimulator:

    def __init__(self, environment, observations, actions=None):

        self._env = environment
        self._observations = observations

        if not actions:
            actions = {
                'up': MoveFactory((0, 1), 10),
                'down': MoveFactory((0, -1), 10),
                'left': MoveFactory((-1, 0), 10),
                'right': MoveFactory((1, 0), 10)
            }
        self._actions = actions

    def timeStep(self):

        observations = self._observations.of(self._env)
        updates = []
        for cell in self._env.cells:
            cellLocation = self._env.cells.locationOf(cell)
            action = cell.act(observations, cellLocation)
            updateFactory = self._actions[action]
            update = updateFactory.produce(cellLocation)
            updates.append(update)
        self.applyRandomly(updates)

    def applyRandomly(self, updates):

            random.shuffle(updates)
            for update in updates: update.apply(self._env)