import numpy as np
import math as math
import matplotlib.pyplot as plt

y = lambda x: (x - 2) ** 2
lower_bound = 0
upper_bound = 7
x0 = 0
epsilon = 0.1

counter_dih = 0
counter_powell = 0
counter_newton = 0


def get_x_by_y(y):
    return math.sqrt(y) + 2


def f(x):
    return (x - 2) ** 2


def df(x):
    return 2 * x - 4


def ddf(x):
    return 2


def dihotom_method(a, b):
    global counter_dih
    counter_dih += 1
    # step 3
    y_k = round((a + b - epsilon) / 2, 12)
    z_k = round((a + b + epsilon) / 2, 12)
    # step 4
    if f(y_k) > f(z_k):
        return dihotom_method(y_k, b)
    else:
        # step 5
        l_k = z_k - a
        # step 5 a
        if l_k <= 2 * epsilon:
            x = (z_k + a) / 2
            return x
        # step 5 b
        else:
            return dihotom_method(a, z_k)


def powell_func_first(y, lower_bound, upper_bound, step):
    # step 1
    x1 = lower_bound
    x2 = lower_bound + step
    # step 2 and 3
    if y(x1) > y(x2):
        x3 = x1 + 2 * step  # 2 - это множитель приращения
    else:
        x3 = x1 - step
    if x3 < x1:
        x1, x2, x3 = x3, x1, x2
    return powell_func_second(y, x1, x2, x3, step)


def powell_func_second(y, x1, x2, x3, step):
    global counter_powell
    counter_powell += 1
    # step 4
    f_min = min(y(x1), y(x2), y(x3))
    x_min = get_x_by_y(f_min)
    # step 5 квадратичная апроксимация
    a1 = (y(x2) - y(x1)) / (x2 - x1)
    a1 = round(a1, 12)
    a2 = (1 / (x3 - x2) * ((y(x3) - y(x1)) / (x3 - x1) - (y(x2) - y(x1)) / (x2 - x1)))
    a2 = round(a2, 12)
    x_quad = ((x2 + x1) / 2) - (a1 / (2 * a2))
    # step 6
    if math.fabs(f_min - y(x_quad)) < epsilon and math.fabs(x_min - x_quad) < epsilon:
        return x_quad
    else:
        # step 7
        x_best = min(math.fabs(x_quad), math.fabs(x_min))
        powell_func_second(y, x_best, x1, x2, step)


def newton_func(x0):
    global counter_newton
    counter_newton += 1
    xn = x0
    # step 2
    xn = xn - df(xn) / ddf(x)
    # step 3
    if abs(df(xn)) <= epsilon:
        # end
        return xn
    else:
        # go to step 2
        newton_func(xn)


# number 1
fig = plt.subplots()
x = np.linspace(-3, 7, 100)
plt.plot(x, y(x))
plt.show()

# number 2
print("Метод Дихотомии = ", dihotom_method(lower_bound, upper_bound))
print("Метод Пауэлла = ", powell_func_first(y, lower_bound, upper_bound, 1))

# number 3
print("Метод Ньютона = ", newton_func(x0))

# number 5
print("Количество итераций для метода Дихотомии = ", counter_dih)
print("Количество итераций для метода Пауэлла = ", counter_powell)
print("Количество итераций для метода Ньютона = ", counter_newton)
