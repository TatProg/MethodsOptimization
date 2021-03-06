from sympy import *
from scipy.optimize import minimize


def function():
    return "x**2 + y**2 - 10*x - 8*y + 3"


def func(x, y):
    return eval(function())


def derivative(x, y, f, h=0.1):
    f1 = "(" + (f.replace("x", ("(" + str(x) + " + " + str(h) + ")"))) + " - " + f + ") / " + str(h)
    f2 = "(" + (f.replace("y", ("(" + str(y) + " + " + str(h) + ")"))) + " - " + f + ") / " + str(h)
    return [eval(f1), eval(f2)]


def gradient(f, x0, e):
    # print(f)
    count = 0
    # print("ГРАДИЕНТНЫЙ МЕТОД")
    while True:
        count = count + 1
        a = 0.2
        x_grad = derivative(x0[0], x0[1], f)
        x_new = [x0[0] - a * x_grad[0], x0[1] - a * x_grad[1]]
        while (func(x0[0], x0[1]) < func(x_new[0], x_new[1])):
            a = a / 2
            x_new = [x0[0] - a * x_grad[0], x0[1] - a * x_grad[1]]
        if (abs(func(x_new[0], x_new[1]) - func(x0[0], x0[1])) < e):
            return x_new
        x0 = x_new
        # print("Новая точка x: " + str(x_new), " " * (40 - len(str(x_new))) + "| Значение функции: " + str(func(x0[0], x0[1])))
    # print("Количество итераций: " + str(count))


def getConfines(confines):
    confines_temp = confines.copy()
    '''
    for i in range(len(confines)):
        confines_temp[i] = "-1 / " + confines_temp[i]
    result = ""
    for i in range(len(confines_temp)):
        result = result + confines_temp[i]
        if (i != len(confines_temp) - 1):
            result = result + " + "
    '''
    for i in range(len(confines_temp)):
        # confines_temp[i] = "((max(0, " + confines_temp[i] + ")) ** 2)"
        confines_temp[i] = "((abs(" + confines_temp[i] + ")) ** 2)"
    result = ""
    for i in range(len(confines_temp)):
        result = result + confines_temp[i]
        if (i != len(confines_temp) - 1):
            result = result + " + "
    return "(" + result + ")"


def getResultOfConfines(f, x, y):
    return eval(f)


x, y = symbols('x y')

conf = [
    "(x + y * 2 - 2)",
    "(2 * x + y - 2)"
]

ε1 = 0.0000001
ε2 = 0.0001
μ = 1000000
B = 0.5
k = 1
x0 = [-1.5, -1]

if __name__ == "__main__":
    while True:
        F_1 = ""
        mas = []
        for i in range(len(conf)):
            mas.append(getResultOfConfines(conf[i], x0[0], x0[1]))
        if (min(mas) < 0):
            F_1 = str(μ) + " * " + getConfines(conf)
            F_1 = str(eval(F_1))
        else:
            F_1 = "0"
        F = function() + " + " + F_1
        # x_new, f_new = newton(F, x0, ε1)
        x_new = gradient(F, x0, ε1)
        x0 = x_new
        if (μ * getResultOfConfines(F_1, x0[0], x0[1]) < ε2):
            break
        μ = μ * B
        k = k + 1
    print("Кол-во итераций: " + str(k))
    print(x0)
    print("Значение функции: " + str(func(x0[0], x0[1])))
