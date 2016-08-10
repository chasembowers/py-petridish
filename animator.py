from matplotlib import pyplot as plt
from matplotlib import animation

class Animator:

    def __init__(self, simulator):
        self._sim = simulator
        self._env = self._sim.environment()

    def _firstFrame(self):
        return self._cells, self._resources

    def _update(self, i):
        self._sim.timeStep()
        print [c.energy() for c in self._env['cells']]
        self._cells.set_data(self._coordinates('cells'))
        self._resources.set_data(self._coordinates('resources'))

        return self._cells, self._resources

    def _coordinates(self, group):
        bodies = self._env[group]
        xs = []
        ys = []
        for body in bodies:
            x, y = self._env.locationOf(body)
            xs.append(x)
            ys.append(y)
        return xs, ys

    def animate(self):

        figure = plt.figure()
        axes = plt.axes(xlim=(-.5, self._env.width()-.5), ylim=(-.5, self._env.height()-.5))
        plt.grid()
        self._cells, = axes.plot([], [], 'ro')
        self._resources, = axes.plot([], [], 'gs')

        anim = animation.FuncAnimation(
            figure,
            self._update,
            init_func=self._firstFrame,
            interval=100,
            blit=True)

        plt.show()