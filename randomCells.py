from animator import Animator
from petridish.actor import RandomActor
from petridish.cell import BasicCell
from petridish.environment import RectangularEnvironment
from petridish.simulator import RandomOrderSimulator


def main():
    env = RectangularEnvironment(50, 50)
    env.insert('cells', BasicCell(RandomActor()), (1,1))
    env.insert('cells', BasicCell(RandomActor()), (26,26))
    env.insert('cells', BasicCell(RandomActor()), (27,27))
    sim = RandomOrderSimulator(env)

    a = Animator(sim)
    a.animate()


if __name__ == '__main__': main()