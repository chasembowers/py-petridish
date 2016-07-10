import unittest
from mock import MagicMock

from petridish.grid_environment import GridEnvironment
from petridish.resource_spawner import UniformResourceSpawner


class TestUniformResourceSpawner(unittest.TestCase):

    _WIDTH = 69
    _HEIGHT = 95
    _ENERGY = 28

    def setUp(self):

        self._spawner = UniformResourceSpawner(energy=self._ENERGY, probSpawn=1)
        self._env = GridEnvironment()
        self._env.width = MagicMock(return_value=self._WIDTH)
        self._env.height = MagicMock(return_value=self._HEIGHT)

    def test_spawnsResourceWithEnergy(self):

        spawnedResources = self._spawner.spawn(self._env)
        assert len(spawnedResources) == 1 and spawnedResources[0].energy() == self._ENERGY

    def test_spawnsInBounds(self):

        for resource in self._spawner.spawn(self._env):
            location = resource.coordinates()
            x,y = location
            assert x >= 0 and x < self._WIDTH
            assert y >= 0 and y < self._HEIGHT

if __name__ == '__main__':
    unittest.main()
