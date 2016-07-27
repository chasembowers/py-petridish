from petridish.grid import FastGrid, Grid


class BasicEnvironment(object):

    def __init__(self, width, height):
        self.cells = FastGrid(width, height)
        self.resources = FastGrid(width, height)