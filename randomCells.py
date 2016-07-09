from animator import Animator
from petridish.actor import RandomActor
from petridish.cell import BasicCell
from petridish.gridenvironment import BasicGridEnvironment


def main():
    env = BasicGridEnvironment(50, 50)
    env.addCell(BasicCell(RandomActor()))
    env.addCell(BasicCell(RandomActor()))
    env.addCell(BasicCell(RandomActor()))

    a = Animator(env)
    a.animate()


if __name__ == '__main__': main()
