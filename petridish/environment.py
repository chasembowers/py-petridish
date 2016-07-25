from petridish.grid import FastGrid


class BasicEnvironment:

    def __init__(self, width, height):
        self.cells = FastGrid(width, height)
        self.resources = FastGrid(width, height)