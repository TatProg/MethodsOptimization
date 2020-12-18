from sympy import *


def function():
    return "x**2 + y**2 - 10*x - 8*y + 3"


def func(x, y):
    return eval(function())


def derivative(x, y, f, h=0.1):
    f1 = "(" + (f.replace("x", ("(" + str(x) + " + " + str(h) + ")"))) + " - " + f + ") / " + str(h)
    f2 = "(" + (f.replace("y", ("(" + str(y) + " + " + str(h) + ")"))) + " - " + f + ") / " + str(h)
    return [eval(f1), eval(f2)]


def gradient(f, x0, e):
    count = 0
    while True:
        count = count + 1
        a = 0.5
        x_grad = derivative(x0[0], x0[1], f)
        x_new = [x0[0] - a * x_grad[0], x0[1] - a * x_grad[1]]
        while func(x0[0], x0[1]) < func(x_new[0], x_new[1]):
            a = a / 2
            x_new = [x0[0] - a * x_grad[0], x0[1] - a * x_grad[1]]
        if abs(func(x_new[0], x_new[1]) - func(x0[0], x0[1])) < e:
            return x_new
        x0 = x_new


def get_confines(confines):
    confines_temp = confines.copy()
    for i in range(len(confines)):
        confines_temp[i] = "-1 / " + confines_temp[i]
    result = ""
    for i in range(len(confines_temp)):
        result = result + confines_temp[i]
        if (i != len(confines_temp) - 1):
            result = result + " + "
    return "(" + result + ")"


def get_res_of_confines(f, x, y):
    return eval(f)


x, y = symbols('x y')

conf = [
    "(x + y * 2 - 2)",
    "(2 * x + y - 2)"
]

epsilon = 0.000001
nu = 1000000
B = 0.5
k = 1
x0 = [0.2, 0.1]
# x0 = [50, 50]

if __name__ == "__main__":
    while True:
        F_1 = ""
        mas = []
        for i in range(len(conf)):
            mas.append(get_res_of_confines(conf[i], x0[0], x0[1]))
        if min(mas) < 0:
            F_1 = str(nu) + " * " + get_confines(conf)
            F_1 = str(eval(F_1))
        else:
            F_1 = "0"
        F = function() + " + " + F_1
        x_new = gradient(F, x0, epsilon)
        x0 = x_new
        if nu * get_res_of_confines(F_1, x0[0], x0[1]) < epsilon:
            break
        nu = nu * B
        k = k + 1
    print("k = " + str(k))
    print("x = ", x0)
    print("f = " + str(func(x0[0], x0[1])))
