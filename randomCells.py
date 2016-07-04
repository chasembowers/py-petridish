from animator import Animator
from petridish.actor import RandomActor
from petridish.cell import Cell
from petridish.gridenvironment import BasicGridEnvironment


def main():
    env = BasicGridEnvironment(50, 50)
    env.addCell(Cell(actor=RandomActor()))
    env.addCell(Cell(actor=RandomActor()))
    env.addCell(Cell(actor=RandomActor()))

    a = Animator(env)
    a.animate()


if __name__ == '__main__': main()
