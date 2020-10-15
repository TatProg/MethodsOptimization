import pylab
from mpl_toolkits.mplot3d import Axes3D
import numpy
from math import *


def f(x):
    fun = 3 * (x[0] - 2) ** 2 + (x[1] - 4) ** 2
    return fun


def count_delta_x(x):
    y = pow(x[0], 2) + pow(x[1], 2)
    y = pow(y, 0.5)
    return y


# step 5
def poisk_po_obrazu(x_prev, x_current):
    x_p = [x_current[0] + (x_current[0] - x_prev[0]), x_current[1] + (x_current[1] - x_prev[1])]
    return x_p


# step 2
def issled_poisk(x0, delta_x):
    x_list = [[], [], [], [], [], [], [], [], []]  # FIXME find better way to write all of this
    x_list[0] = x0
    x_list[1] = [x0[0] + delta_x[0], x0[1] + delta_x[1]]  # 1 quarter
    x_list[2] = [x0[0] - delta_x[0], x0[1] + delta_x[1]]  # 2 quarter
    x_list[3] = [x0[0] - delta_x[0], x0[1] - delta_x[1]]  # 3 quarter
    x_list[4] = [x0[0] + delta_x[0], x0[1] - delta_x[1]]  # 4 quarter
    x_list[5] = [x0[0], x0[1] + delta_x[1]]  # 1-2 half
    x_list[6] = [x0[0] - delta_x[0], x0[1]]  # 2-3 half
    x_list[7] = [x0[0], x0[1] - delta_x[1]]  # 3-4 half
    x_list[8] = [x0[0] + delta_x[0], x0[1]]  # 4-1 half
    f_x_list = []
    for i in range(len(x_list)):
        f_x_list.append(x_list[i])
    x_test = x_list[1]
    for i in range(1, len(x_list)):
        if x_test > x_list[i]:
            x_test = x_list[i]
    f_x_test = f(x_test)
    # step 3
    if f_x_test > f_x_list[0]:
        # step 5
        print()
    else:
        # step 4
        end_of_search(x_test, delta_x)


# step 4
def end_of_search(x, delta_x):
    if count_delta_x(x) < 0.1:  # TODO add iteration limit = 10
        # end of search
        print(x)
        return x
    else:
        # go to step 2
        delta_x[0] /= 2  # TODO change 2 for a from word doc
        delta_x[1] /= 2
        # iterations += 1
        issled_poisk(x, delta_x)


x0 = [0, 1]
delta_x = [2, 2]
a = 2
e = 0.1
fx0 = f(x0)
# на сайте интуита сказано, что удовлетворительным является
# уменьшение шага (шагов) в десять раз от начальной длины
# поэтому ограничение на шаги будет 10
iterations = 0

