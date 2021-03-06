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
def issled_poisk(x0, delta_x, iterations):
    x_list = []
    for i in range(9):
        x_list.append([])
        for j in range(2):
            x_list[i].append([])
    x_list[0][0] = x0
    x_list[1][0] = [x0[0] + delta_x[0], x0[1] + delta_x[1]]  # 1 quarter
    x_list[2][0] = [x0[0] - delta_x[0], x0[1] + delta_x[1]]  # 2 quarter
    x_list[3][0] = [x0[0] - delta_x[0], x0[1] - delta_x[1]]  # 3 quarter
    x_list[4][0] = [x0[0] + delta_x[0], x0[1] - delta_x[1]]  # 4 quarter
    x_list[5][0] = [x0[0], x0[1] + delta_x[1]]  # 1-2 half
    x_list[6][0] = [x0[0] - delta_x[0], x0[1]]  # 2-3 half
    x_list[7][0] = [x0[0], x0[1] - delta_x[1]]  # 3-4 half
    x_list[8][0] = [x0[0] + delta_x[0], x0[1]]  # 4-1 half
    for i in range(9):
        x_list[i][1] = f(x_list[i][0])
    i = 1
    for n in range(1, 9):
        if x_list[i][1] > x_list[n][1]:
            i = n
    if x_list[i][1] > x_list[0][1]:
        # step 5
        super_point = [x_list[0][0], x_list[i][0]]
        return super_point
        # return x_zero, x_point  #fixed? TypeError: cannot unpack non-iterable NoneType object
    else:
        # step 4
        end_of_search(x_list[i][0], delta_x, iterations)


# step 4
def end_of_search(x, delta_x, iterations):
    iterations += 1
    if iterations == 10:
        # end of search because of operation limits
        print("end of search because of operation limits", x)
        exit()
    else:
        if count_delta_x(x) < 0.1:  # TODO change 0.1 for a from word doc
            # end of search
            print("delta_x lower than e", x)
            exit()
        else:
            # go to step 2
            delta_x[0] /= 2  # TODO change 2 for a from word doc
            delta_x[1] /= 2
            # issled_poisk(x, delta_x)
            step_2(x, delta_x, iterations)


def step_6(x0, x, delta_x, iterations):
    xp = poisk_po_obrazu(x0, x)
    f_xp = f(xp)
    super_point = issled_poisk(xp, delta_x, iterations)
    x_zero = super_point[0]
    x_k_plus_1 = super_point[1]
    if f(x_k_plus_1) < f(x):
        # go to step 5
        step_6(x, x_k_plus_1, delta_x, iterations)
    else:
        # go to step 4
        end_of_search(x, delta_x)  # FIXED? TypeError: cannot unpack non-iterable NoneType object


def step_2(x0, delta_x, iterations):
    super_point = issled_poisk(x0, delta_x, iterations)
    x_zero = super_point[0]
    x_test = super_point[1]
    step_6(x_zero, x_test, delta_x, iterations)


x0 = [0, 1]
delta_x = [2, 2]
#     a = 2
#     e = 0.1
#     fx0 = f(x0)
#     # на сайте интуита сказано, что удовлетворительным является
#     # уменьшение шага (шагов) в десять раз от начальной длины
#     # поэтому ограничение на шаги будет 10
iterations = 0
step_2(x0, delta_x, iterations)
