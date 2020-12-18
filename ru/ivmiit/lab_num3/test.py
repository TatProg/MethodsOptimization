import numpy as np
import pylab
from mpl_toolkits.mplot3d import Axes3D


# main function
def f_x(x):
    result = x[0] ** 2 + x[1] ** 2 - 10 * x[0] - 8 * x[1] + 3
    return result
    # return round(result, 12)


# Находим градиент
def gradient(func, x, h):
    return [
        (func([x[0] + h, x[1]]) - func(x)) / h,
        (func([x[0], x[1] + h]) - func(x)) / h
    ]


# # График. Копипаста из предыдущей лабы
# def makeData(func):
#     x = np.arange(-10, 10, 1)
#     y = np.arange(-10, 10, 1)
#     xgrid, ygrid = np.meshgrid(x, y)
#     zgrid = func([xgrid, ygrid])
#     return xgrid, ygrid, zgrid


# def draw(func):
#     x, y, z = makeData(func)
#     fig = plt.figure()
#     ax = Axes3D(fig)
#     ax.plot_surface(x, y, z)
#     plt.show()


def show_function():
    x1 = np.arange(-5, 15, 0.1)
    x2 = np.arange(-5, 15, 0.1)
    x_grid, y_grid = np.meshgrid(x1, x2)
    z_grid = x_grid ** 2 + y_grid ** 2 - 10 * x_grid - 8 * y_grid + 3
    return x_grid, y_grid, z_grid


def min_by_gradient(func, x_0):
    grad = gradient(func, x_0, 0.0000001)
    x = np.copy(x_0)
    step = 0.0001
    while True:
        f_k = func(x)
        x_prev = np.copy(x)
        x[0] -= grad[0] * step
        x[1] -= grad[1] * step
        f_k1 = func(x)
        if (f_k1 >= f_k):
            return x_prev


def cauch_search(func, x_0, e):
    x = np.copy(x_0)
    while True:
        f_prev = func(x)
        x_next = min_by_gradient(func, x)
        f_cur = func(x_next)
        if np.abs(f_cur - f_prev) < e:
            return x_next
        x = x_next


# Метод штрафов (к ЦФ добавляется ф-ия, к-ая пред
# собой штраф за наруш кажд огр-ия
# к осн ф-иии доб доп огр-ие, те штрафная ф-ия
def shtraff(func, D, x_0, e, wh):
    nu = 0.0001
    beta = 1.1
    k = 1
    x = np.copy(x_0)

    def B(D, x):
        res = 0
        for i in range(0, len(D)):
            res = res + D[i](x)
        return res

    # 
    while k <= wh:
        # 
        x_in_D = True
        f = lambda x: func(x)
        for i in range(0, len(D)):
            x_in_D = x_in_D and D[i](x) <= 0
        if not x_in_D:
            # 
            f = lambda x: func(x) + nu * B(D, x)
        x = cauch_search(f, x, 0.01)
        b = B(D, x)
        # 
        if nu * b < e:
            break
            # 
        nu = beta * nu
        k += 1
    return x, func(x), k


#
def barrier(func, D, x_0, e, wh):
    nu = 100
    beta = 0.1
    k = 1
    x = np.copy(x_0)

    # 
    def B(D, x):
        res = 0
        for i in range(0, len(D)):
            # 
            if D[i](x) == 0:
                return 0
        res -= 1 / D[i](x)
        return res

    #
    while k <= wh:
        #
        f = lambda x: func(x) + nu + B(D, x)
        #
        x = cauch_search(f, x, 0.1)
        #
        if nu * B(D, x) < e:
            break
        nu = beta * nu
        k += 1

        return x, func(x), k


e = 0.0001
x_0 = [10, 20]
wh = 500
k = 100
nu = 100000

D = [
    lambda x: x[0] + x[1] * 2 - 2,
    lambda x: x[0] * 2 + x[1] - 2
]



x, y, z = show_function()
fig = pylab.figure()
axes = Axes3D(fig)
axes.plot_surface(x, y, z)
pylab.show()

print(shtraff(f_x, D, x_0, e, wh))
print(barrier(f_x, D, x_0, e, wh))
