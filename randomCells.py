from animator import Animator
from petridish.actor import RandomActor
from petridish.cell import BasicCell
from petridish.grid_environment import BasicGridEnvironment


def main():
    env = BasicGridEnvironment(50, 50)
    env.addCell(BasicCell(RandomActor()), randLocation=True)
    env.addCell(BasicCell(RandomActor()), randLocation=True)
    env.addCell(BasicCell(RandomActor()), randLocation=True)

    a = Animator(env)
    a.animate()


if __name__ == '__main__': main()
