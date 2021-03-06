import matplotlib.pyplot as plt
import numpy as np
import math

h = 0.0000001


def f(x):
    return ((x[0] - x[1]) ** 2 + (x[0] ** 2 + 20 - x[1] + 4) ** 2) ** 1 / 2


def grad_f(func, x):
    return [
        (func([x[0] + h, x[1]]) - func(x)) / h,
        (func([x[0], x[1] + h]) - func(x)) / h
    ]


def grad_speed(grad):
    return math.sqrt((grad[0] * grad[0] + grad[1] * grad[1]))


def draw(f):
    x = np.arange(-5, 5, 0.5)
    y = np.arange(-10, 10, 1)
    xgrid, ygrid = np.meshgrid(x, y)
    z = f([xgrid, ygrid])
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.contourf(x, y, z, cmap='Spectral', alpha=0.7)
    return ax


def df_dx1(func, x):
    return (func([x[0] + h, x[1]]) - func(x)) / h


def df_dx2(func, x):
    return (func([x[0], x[1] + h]) - func(x)) / h


def d2f_dx1x1(func, x):
    return (df_dx1(func, [x[0] + h, x[1]]) - df_dx1(func, x)) / h


def d2f_dx2x2(func, x):
    return (df_dx2(func, [x[0], x[1] + h]) - df_dx2(func, x)) / h


def d2f_dx1x2(func, x):
    return (df_dx1(func, [x[0], x[1] + h]) - df_dx1(func, x)) / h


def matrix_hesse(func, x):
    return (
        (d2f_dx1x1(func, x), d2f_dx1x2(func, x)),
        (d2f_dx1x2(func, x), d2f_dx2x2(func, x))
    )


def next_x(func, x, d):
    curr = func(x)
    t = 0
    lam = 0.1
    while True:
        t += lam
        prev = curr
        x_curr = x + t * d
        curr = func(x_curr)
        if curr >= prev:
            return x_curr - lam * d


def search_newton(func, x0):
    eps1 = 0.1
    eps2 = 0.1
    M = 100
    k = 1
    x = x0
    track = [x]

    while True:
        grad = grad_f(func, x)
        if (grad_speed(grad) < eps1) or (k >= M):
            return x, k, track
        H = matrix_hesse(func, x)
        H_1 = np.linalg.inv(H)

        if (H_1[0, 0] > 0) and (np.linalg.det(H_1) > 0):
            d = -1 * np.dot(H_1, grad)
        else:
            d = -1 * grad
        x_next = next_x(func, x, d)

        if (np.linalg.norm(x_next - x) <= eps2) and (abs(func(x_next) - func(x) <= eps2)):
            return x_next, k, track
        x = x_next
        track.append(x)
        k = k + 1


def search_marquardt(func, x0):
    eps1 = 0.1
    eps2 = 0.1
    M = 1000
    k = 1
    x = x0
    track = [x]
    lam = 100

    while True:
        grad = grad_f(func, x)
        if (grad_speed(grad) < eps1) or (k >= M):
            return x, k, track
        H = matrix_hesse(func, x)
        while True:
            H = H + lam * np.eye(2)
            H_1 = np.linalg.inv(H)
            d = -1 * np.dot(H_1, grad)
            x_next = x + d
            if func(x_next) < func(x):
                k = k + 1
                x = x_next
                track.append(x)
                lam = lam / 2
                break
            lam = 2 * lam


print('Метод Ньютона-Рафсона:')
x, n, track = search_newton(f, [1.0, 1.0])
track = np.array(track)
print('x= ', x, 'f= ', f(x), 'количество итераций=', n)
ax = draw(f)
ax.view_init(90, 0)
ax.plot3D(track[:, 0], track[:, 1], f([track[:, 0], track[:, 1]]), color='black')
ax.scatter3D(track[:, 0], track[:, 1], f([track[:, 0], track[:, 1]]), color='black')
print('Метод Марквардта:')
x, n, track = search_marquardt(f, [1.0, 1.0])
track = np.array(track)
print('x= ', x, 'f= ', f(x), 'количество итераций=', n)
ax.plot3D(track[:, 0], track[:, 1], f([track[:, 0], track[:, 1]]), color='green')
ax.scatter3D(track[:, 0], track[:, 1], f([track[:, 0], track[:, 1]]), color='green')
plt.show()
print('Координаты точки минимума:')
# print('x=[', 1 / 2, ',', 43 / 8, ']')
