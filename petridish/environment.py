from petridish.grid import FastGrid

class Environment(object): pass

class BasicEnvironment(Environment):

    def __init__(self, width, height):
        self.cells = FastGrid(width, height)
        self.resources = FastGrid(width, height)