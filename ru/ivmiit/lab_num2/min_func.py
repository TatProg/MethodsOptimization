import pylab
from mpl_toolkits.mplot3d import Axes3D
import numpy
import numpy as np
import matplotlib
from math import *


def show_function():
    x1 = numpy.arange(-10, 10, 0.1)
    x2 = numpy.arange(-10, 10, 0.1)
    x_grid, y_grid = numpy.meshgrid(x1, x2)

    z_grid = 3 * (x_grid - 2) ** 2 + (y_grid - 4) ** 2
    return x_grid, y_grid, z_grid


def main_func_test(x_grid, y_grid):
    z_grid = 3 * (x_grid - 2) ** 2 + (y_grid - 4) ** 2
    return z_grid


def main_func(x):
    f = 3 * (x[0] - 2) ** 2 + (x[1] - 4) ** 2
    return f


def count_delta_x(x):
    y = pow(x[0], 2) + pow(x[1], 2)
    y = pow(y, 0.5)
    return y


# step 2
def issled_poisk(x_0, delta_x):
    f_x = [[], [], [], [], [], [], [], [], []]  # FIXME find better way to write all this
    f_x[0] = x_0
    f_x[1] = [x_0[0] + delta_x[0], x_0[1] + delta_x[1]]  # 1 quarter
    f_x[2] = [x_0[0] - delta_x[0], x_0[1] + delta_x[1]]  # 2 quarter
    f_x[3] = [x_0[0] - delta_x[0], x_0[1] - delta_x[1]]  # 3 quarter
    f_x[4] = [x_0[0] + delta_x[0], x_0[1] - delta_x[1]]  # 4 quarter
    f_x[5] = [x_0[0], x_0[1] + delta_x[1]]  # 1-2 half
    f_x[6] = [x_0[0] - delta_x[0], x_0[1]]  # 2-3 half
    f_x[7] = [x_0[0], x_0[1] - delta_x[1]]  # 3-4 half
    f_x[8] = [x_0[0] + delta_x[0], x_0[1]]  # 4-1 half
    # for i in range(2):
    #     for j in range(2):
    #         point_num += 1
    #         # f_x[point_num] = [x_0[0] + i * 2, x_0[1] + j * 2]   #FIXME change two for smth else
    #         f_x[point_num][0] = x_0[0] + i * 2,
    #         f_x[point_num][0] = x_0[1] + j * 2
    f_x_test = f_x[0]
    for n in range(len(f_x)):
        q = main_func(f_x[n])
        p = main_func(f_x_test)
        if q < p:
            # if main_func(f_x[n]) > main_func(f_x_test):
            print("old ", f_x[n], ". new ", f_x_test)
            f_x_test = f_x[n]
    # step 3
    a = main_func(f_x_test)
    b = main_func(f_x[0])
    if a < b:
        # if main_func(f_x_test) < main_func(f_x[0]):
        # go to step 5
        print("old f(x)", a, ". new f(x)", b)
        poisk_po_obraz(f_x[0], f_x_test, delta_x)
    else:
        # go to step 4
        end_of_search(f_x_test, delta_x)
    return f_x_test
    # if f_x[0] > main_func(x_0):
    #     # step 4
    #     # f_x_zero = f_x[0]
    #     # if delta_x < e:
    #     if pow(pow(f_x[0][0], 2) + pow(f_x[0][1], 2), 0.5) < e:
    #         return f_x[0]
    #     else:
    #         delta_x[0] = delta_x[0] / a
    #         delta_x[1] = delta_x[1] / a
    #         issled_poisk(f_x[0], delta_x)
    # else:
    #     # step 5
    #     # poisk_po_obraz()
    #     print()


# step 5 and step 6
def poisk_po_obraz(x_prev, x_current, delta_x):
    # step 5
    x_p = [x_current[0] + (x_current[0] - x_prev[0]), x_current[1] + (x_current[1] - x_prev[1])]
    # step 6
    x_p_test = issled_poisk(x_p, delta_x)
    # step 7
    if main_func(x_p_test) < main_func(x_p):
        # go to step 5 (and 6-7)
        poisk_po_obraz(x_p, x_p_test, delta_x)
    else:
        # go to step 4
        end_of_search(x_p_test, delta_x)


# step 4
def end_of_search(x_p, delta_x):
    if count_delta_x(x_p) < 0.1:  # TODO change 0.1 for e from word doc
        # end
        print(x_p)
        return x_p
    else:
        # go to step 2
        delta_x[0] /= 2  # TODO change 2 for a from word doc
        delta_x[1] /= 2
        issled_poisk(x_p, delta_x)  # TODO change 2 and 0.1 for a and e from word doc
    # f_x_p = main_func(x_p)
    # f_x = main_func(x_current)
    # x_prev = x_current
    # if f_x_p < f_x:
    #     x_current = x_p
    #     f_x = f_x_p
    #     issled_poisk(x_p)
    #
    #     # some code
    #
    #     # if f_x_plus1  < f_x
    #
    #     # yes - step 5
    #     # poisk_po_obraz(x_plux1)
    #
    #     # no - step 4
    #     # if pow(pow(x_plux1[0], 2) + pow(x_plux1[1], 2), 0.5) < e:
    #     #     return x_plux1
    #     # else:
    #     #     delta_x[0] = delta_x[0] / a
    #     #     delta_x[1] = delta_x[1] / a
    #     #     issled_poisk(x_plux1, delta_x)


def hooke_jeeves_test(x_0, delta_x):
    # some shit with f_x_zero and f_x_0
    f_x_0 = main_func(x_0)
    x_test = issled_poisk(x_0, delta_x)
    f_x_test = main_func(x_test)
    if f_x_test < f_x_0:
        poisk_po_obraz(x_0, x_test, delta_x)


def hooke_jeeves_show():
    x_0 = [0, 1]
    delta_x = [2, 2]
    hooke_jeeves_test(x_0, delta_x)


def show_image():
    x, y, z = show_function()
    fig = pylab.figure()
    axes = Axes3D(fig)
    axes.plot_surface(x, y, z)
    pylab.show()


f_x_zero = main_func([0, 1])
hooke_jeeves_show()
