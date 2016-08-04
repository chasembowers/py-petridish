import unittest
from petridish.actor import RandomActor
from petridish.simulator import DEFAULT_ACTIONS


class TestRandomActor(unittest.TestCase):

    def setUp(self):

        self.randomActor = RandomActor()

    def test_returnsValidAction(self):

        self.assertIn(self.randomActor.act(None, None, None), DEFAULT_ACTIONS)

    def test_producesChild(self):

        child = self.randomActor.child()
        self.assertEqual(type(child), RandomActor)
        self.assertNotEqual(child, self.randomActor)

if __name__ == '__main__':
    unittest.main()