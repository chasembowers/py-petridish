import unittest
from mock import MagicMock

from petridish.energized import Energized
from petridish.grid_environment import GridEnvironment
from petridish.resource_spawner import UniformResourceSpawner


class TestUniformResourceSpawner(unittest.TestCase):

    _WIDTH = 69
    _HEIGHT = 95

    def setUp(self):

        self._energized = Energized()

        self._spawner = UniformResourceSpawner(energized=self._energized, probSpawn=1)
        self._env = GridEnvironment()
        self._env.width = MagicMock(return_value=self._WIDTH)
        self._env.height = MagicMock(return_value=self._HEIGHT)

        self._energized.consumeEnergy = MagicMock()
        self._energized.releaseEnergy = MagicMock()
        self._energized.energy = MagicMock(return_value=87)

    def test_spawnsResourceWithEnergy(self):

        spawnedResources = self._spawner.spawn(self._env)
        assert len(spawnedResources) == 1
        assert type(spawnedResources[0]._myEnergy) == type(self._energized)
        assert spawnedResources[0]._myEnergy.energy() == self._energized.energy()

    def test_spawnsInBounds(self):

        for resource in self._spawner.spawn(self._env):
            location = resource.coordinates()
            x,y = location
            assert x >= 0 and x < self._WIDTH
            assert y >= 0 and y < self._HEIGHT

if __name__ == '__main__':
    unittest.main()
