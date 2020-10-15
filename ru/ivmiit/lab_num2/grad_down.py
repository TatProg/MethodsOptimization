import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import minimize

b = 0.1
e = 0.1


# x_0 = [0, 1]


# целевая функция
def func(x):
    f = 3 * (x[0] - 2) ** 2 + (x[1] - 4) ** 2
    return f


# функц вычисления градиента целевой функции
def func_deriv(x):
    dfdx0 = 6 * x[0] - 12
    dfdx1 = 2 * x[1] - 8
    return np.array([dfdx0, dfdx1])


# # массив функций, задающих мно-во доп-ых ешение
# cons = (
#     # {'type': 'ineq', 'fun': lambda x: np.array([-x[0] - x[1] + 3]), 'jac': lambda x: np.array([-1.0, -1.0])},
#     # {'type': 'ineq', 'fun': lambda x: np.array([2 * x[0] - 3 * x[1] - 6]), 'jac': lambda x: np.array([2.0, -3.0])},
#     {'type': 'ineq', 'fun': lambda x: np.array(x[0]), 'jac': lambda x: np.array([1.0, 0.0])},   # FIXME is it [0, 0] ver 1
#     {'type': 'ineq', 'fun': lambda x: np.array(x[1]), 'jac': lambda x: np.array([0.0, 1.0])},   # FIXME is it [0, 0] ver 2
# )
# # res = minimize(fun=func, x0=[1.0, 1.0], jac=func_deriv)
# # print(res)
# x0_bound = (0, np.inf)
# x1_bound = (0, np.inf)
# res = minimize(fun=func, x0=[1.0, 1.0], jac=func_deriv, bounds=(x0_bound, x1_bound), constraints=cons)


# # Метод вычисления лямбды
# def calculate_delta(point, agrad):
#     dividend = 4 * point[0] * agrad[0] + 10 * point[1] * agrad[1] - 4 * point[0] * agrad[1] - 4 * point[1] * agrad[
#         0] + 2 * agrad[0] - 8 * agrad[1]
#     divider = -4 * agrad[0] * agrad[0] - 10 * agrad[1] * agrad[1] + 8 * agrad[0] * agrad[1]
#     return - dividend / divider


# проверка на градиента на ноль
def is_null(array):
    for i in range(len(array)):
        if abs(array[i]) > 0.01:
            return False
    return True


# Метод вычисления новой точки
def calculate_next_point(point, grad):
    agrad = np.negative(grad)
    delta = 0.1
    next_point = []
    for i in range(len(point)):
        next_point.append(point[i] + delta * agrad[i])
    return np.array(next_point)


# # график
# ygraph = []
# xgraph = []
# line = [0, 100]
# for i in range(1000):
#     xgraph.append(i)
#     t = [0, 1]
#     ygraph.append(func(t))
# plt.plot(xgraph, ygraph)
# plt.show()

# x_arr = [[0, 0], [0, 1], [1, 0]]
# for i in range(len(x_arr)):
#     k = 0
#     curr_x = x_arr[i]
#     while True:
#         gradient = func_deriv(curr_x)  # Вычисляем градиент, подставив точку
#         if is_null(gradient):  # Проверка частных случаев
#             break
#         # Нахождение новой точки
#         curr_x = calculate_next_point(curr_x, gradient)  # Вычисление след итерац точки
#         k += 1
#         if k == 3:
#             break
#     print("Точка: " + str(x_arr[i]))
#     print("x = " + str(curr_x))
#     print("iterated = " + str(k))
#     print()


def gradient_down(x_0, x_1):
    f_x_0 = func_deriv(x_0)
    for i in range(len(x_1)):
        x_1[i] = x_0[i] - b * f_x_0[i]
        x_1[i] = round(x_1[i], 12)
    return x_0, x_1


def gradient_show():
    x_0 = [0, 1]
    x_1 = [0, 1]
    x_0, x_1 = gradient_down(x_0, x_1)
    ite = 1
    while abs(func(x_1) - func(x_0)) > e:
        ite += 1
        x_1, x_0 = gradient_down(x_0, x_1)
    # print(ite)
    print(x_1)


gradient_show()
