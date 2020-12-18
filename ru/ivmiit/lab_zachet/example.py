import matplotlib as plt
import numpy as np

def f_x(x):
	return ((x[0] - x[1])**2 + (x[0]**2 + a - x[1]**2 - b)**2) ** (1/2)


def gradient(func, x):
    return [
        (func([x[0] + h, x[1]]) - func(x)) / r,
        (func([x[0], x[1] + h]) - func(x)) / r
    ]


def check_exit(grad):
	return(grad[0] ** 2 + grad[1]**)