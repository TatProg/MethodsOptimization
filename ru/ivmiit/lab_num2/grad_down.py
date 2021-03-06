import numpy as np
import pylab
from mpl_toolkits.mplot3d import Axes3D
import numpy
from math import *

# Значение из ворд документа
b = 0.1
e = 0.1


# целевая функция из ворд документа
def func(x):
    f = 3 * (x[0] - 2) ** 2 + (x[1] - 4) ** 2
    return f


# функц вычисления градиента целевой функции - сделал производную по x1 и по x2
def func_deriv(x):  # FIXME формула производной из 1 презы 65-66 слайды
    # dfdx0 = 6 * x[0] - 12
    # dfdx1 = 2 * x[1] - 8
    # return np.array([dfdx0, dfdx1])
    x_low = [0, 0]
    x_up = [0, 0]
    dfdx = [0, 0]
    for i in range(2):
        x_low[i] = x[i] - b
        x_up[i] = x[i] + b
        dfdx[i] = (func(x_up) - func(x_low)) / (2 * b)
    return dfdx


def gradient_down(x_0, x_1):
    f_x_0 = func_deriv(x_0) # FIXME !!!
    for i in range(len(x_1)):
        # step 2. Формула со слайда №33
        x_1[i] = x_0[i] - b * f_x_0[i]
        x_1[i] = round(x_1[i], 12)
    return x_0, x_1


def gradient_show():
    x_0 = [0, 1]
    x_1 = [0, 1]
    x_0, x_1 = gradient_down(x_0, x_1)
    iteration = 1
    # step 3. Пятая формула со слайда №31
    while abs(func(x_1) - func(x_0)) > e:
        iteration += 1
        x_1, x_0 = gradient_down(x_0, x_1)
    # print(iteration)
    print(x_1)


# говнокод (функция) чисто чтобы график работал
def show_function():
    x1 = numpy.arange(-10, 10, 0.1)
    x2 = numpy.arange(-10, 10, 0.1)
    x_grid, y_grid = numpy.meshgrid(x1, x2)

    z_grid = 3 * (x_grid - 2) ** 2 + (y_grid - 4) ** 2
    return x_grid, y_grid, z_grid


# Начало программного кода
gradient_show()

# 1 задание - постройка графика
x, y, z = show_function()
fig = pylab.figure()
axes = Axes3D(fig)
axes.plot_surface(x, y, z)
pylab.show()
