import unittest

from petridish.environment import Environment
from petridish.observe import NullObservations
from petridish.observe import NullObserver


class TestNullObserver(unittest.TestCase):

    def test_introspect(self):
        env = Environment()
        obs = NullObserver().observe(env)
        self.assertEqual(type(obs), NullObservations)

if __name__ == '__main__':
    unittest.main()

