import unittest

from petridish.environment import Environment
from petridish.observations import IdentityObservations


class TestIdentityObserver(unittest.TestCase):

    def test_construction(self):
        env = Environment()
        observations = IdentityObservations.of(env)
        self.assertEqual(observations, IdentityObservations(env))

if __name__ == '__main__':
    unittest.main()

