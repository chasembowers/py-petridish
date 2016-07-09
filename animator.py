from matplotlib import pyplot as plt
from matplotlib import animation

class Animator:

    def __init__(self, env):
        self._env = env
        self._cells = env.cells()
        self._circles = [plt.Circle(c.coordinates(), .5) for c in self._cells]

    def _firstFrame(self):
        for c in self._circles: c.set_visible(False)
        return self._circles

    def _update(self, i):
        self._env.timeStep()
        if i == 1:
            for c in self._circles: c.set_visible(True)
        for i in range(len(self._circles)):
            self._circles[i].center = self._cells[i].coordinates()
        return self._circles

    def animate(self):

        figure = plt.figure()
        axes = plt.axes(xlim=(-.5, self._env.width()-.5), ylim=(-.5, self._env.height()-.5))
        plt.grid()
        for c in self._circles: axes.add_patch(c)

        anim = animation.FuncAnimation(
            figure,
            self._update,
            init_func=self._firstFrame,
            interval=100,
            blit=True)

        plt.show()
