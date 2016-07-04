import unittest
from mock import MagicMock

from petridish.gridenvironment import BasicGridEnvironment
from petridish.cell import Cell


class TestBasicGridEnvironment(unittest.TestCase):

    _WIDTH = 123
    _HEIGHT = 456

    def setUp(self):

        self._env = BasicGridEnvironment(self._WIDTH, self._HEIGHT)
        self._body = Cell()
        self._env.addCell(self._body)

        self._body.moveLeft = MagicMock()
        self._body.moveRight = MagicMock()
        self._body.moveUp = MagicMock()
        self._body.moveDown = MagicMock()
        self._body.act = MagicMock(return_value=None)

    def moveHelper(self, direction):
        self._body.act = MagicMock(return_value=direction)
        self._env.timeStep()
        if direction == 'left': self._body.moveLeft.assert_called_with()
        elif direction == 'right': self._body.moveRight.assert_called_with()
        elif direction == 'up': self._body.moveUp.assert_called_with()
        elif direction == 'down': self._body.moveDown.assert_called_with()

    def test_moveLeft(self): self.moveHelper('left')

    def test_moveRight(self): self.moveHelper('right')

    def test_moveUp(self): self.moveHelper('up')

    def test_moveDown(self): self.moveHelper('down')

    def test_outOfLeftBound(self):
        self._body.isLeftOf = MagicMock(side_effect=lambda x: x == 0)
        self._env.timeStep()
        self._body.moveRight.assert_called_with()

    def test_outOfRightBound(self):
        self._body.isRightOf = MagicMock(side_effect=lambda x: x == self._WIDTH - 1)
        self._env.timeStep()
        self._body.moveLeft.assert_called_with()

    def test_outOfLowerBound(self):
        self._body.isBelow = MagicMock(side_effect=lambda x: x == 0)
        self._env.timeStep()
        self._body.moveUp.assert_called_with()

    def test_outOfUpperBound(self):
        self._body.isAbove = MagicMock(side_effect=lambda x: x == self._HEIGHT - 1)
        self._env.timeStep()
        self._body.moveDown.assert_called_with()

if __name__ == '__main__':
    unittest.main()
