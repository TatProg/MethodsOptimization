import numpy as np
import pylab
from mpl_toolkits.mplot3d import Axes3D


def make_data(func, x=None, y=None):
    if x is None:
        x = np.arange(-6, 15, 1)
    if y is None:
        y = np.arange(-5, 20, 1)
    xgrid, ygrid = np.meshgrid(x, y)

    zgrid = func([xgrid, ygrid])
    return xgrid, ygrid, zgrid


def draw(func, x=None, y=None):
    x, y, z = make_data(func, x, y)

    fig = pylab.figure()
    ax = Axes3D(fig)
    ax.plot_wireframe(x, y, z)
    return ax


func = lambda x: ((x[0] - x[1]) ** 2 + (x[0] ** 2 + 3 - x[1] - 17) ** 2) ** 0.5

_arr_NR = []
_arr_M = []
f = open('NR.txt', 'r')
for line in f:
    _arr_NR.append(float(line))
f = open('M.txt', 'r')
for line in f:
    _arr_M.append(float(line))

z_NR = []
for i in range(len(_arr_NR) // 2):
    z_NR.append(func([_arr_NR[2 * i], _arr_NR[2 * i + 1]]))
z_M = []
for i in range(len(_arr_M) // 2):
    z_M.append(func([_arr_M[2 * i], _arr_M[2 * i + 1]]))

ax = draw(func)
ax.view_init(90, 0)

ax.plot3D(_arr_NR[:: 2], _arr_NR[1:: 2], z_NR, color='red')
ax.scatter3D(_arr_NR[:: 2], _arr_NR[1:: 2], z_NR, color='pink')

ax.plot3D(_arr_M[:: 2], _arr_M[1:: 2], z_M, color='green')
ax.scatter3D(_arr_M[:: 2], _arr_M[1:: 2], z_M, color='yellow')
pylab.show()
