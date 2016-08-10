import random

from petridish.observe import NullObserver
from petridish.update_factory import MoveFactory

DEFAULT_ACTIONS = {
        'up': MoveFactory((0, 1), 10),
        'down': MoveFactory((0, -1), 10),
        'left': MoveFactory((-1, 0), 10),
        'right': MoveFactory((1, 0), 10)
    }

class Simulator(object):

    def timeStep(self): raise NotImplementedError()

    def environment(self): raise NotImplementedError()

class RandomOrderSimulator(Simulator):

    def __init__(self, environment, observer=None, actions=None, stepUpdates=None):

        self._env = environment

        if not observer: observer = NullObserver()
        self._observer = observer
        if not actions: actions = DEFAULT_ACTIONS
        self._actions = actions
        if not stepUpdates: stepUpdates = []
        self._stepUpdates = stepUpdates

    def timeStep(self):

        observations = self._observer.observe(self._env)
        updates = []
        for cell in self._env['cells']:
            cellLocation = self._env.locationOf(cell)
            action = cell.act(observations, cellLocation)
            updateFactory = self._actions[action]
            update = updateFactory.produce(cellLocation)
            updates.append(update)
        self._applyRandomly(updates)
        for update in self._stepUpdates: update.apply(self._env)

    def _applyRandomly(self, updates):

            random.shuffle(updates)
            for update in updates: update.apply(self._env)

    def environment(self): return self._env