import unittest

from petridish.cell import Cell
from petridish.introspect import NullIntrospector, NullIntrospection


class TestNullIntrospector(unittest.TestCase):

    def test_introspect(self):
        cell = Cell()
        introspection = NullIntrospector().introspect(cell)
        self.assertEqual(type(introspection), NullIntrospection)


if __name__ == '__main__':
    unittest.main()
