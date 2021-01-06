import numpy as np

test_matrix = np.array([
    [10, 20, 30, 40],
    [100, 90, 80, 70],
    [50, 15, 25, 60],
    [95, 55, 25, 45]
])


def reduction_strings(matrix):
    for i in range(matrix.shape[0]):
        min_elem_string = min(matrix[i, :])
        # print(matrix[i, :], " and min is ", min_elem_string)
        for k in range(len(matrix[i, :])):
            matrix[i][k] -= min_elem_string
    return matrix


def reduction_columns(matrix):
    for j in range(matrix.shape[1]):
        min_elem_column = min(matrix[:, j])
        for k in range(len(matrix[:, j])):
            matrix[k][j] -= min_elem_column
    return matrix


def check_zero(matrix):
    flag = True
    for i in range(matrix.shape[0]):
        if min(matrix[i, :]) != 0:
            flag = False
    for j in range(matrix.shape[1]):
        if min(matrix[:, j]) != 0:
            flag = False
    return flag


def calc_adjacent_zero(matrix):
    # Идея моего алгоритма в том, чтобы проверить все нули, на наличие соседей нулей
    # Если у нуля много соседей - можно вычеркнуть, не потеряв много других цифр
    # Ввиду костыльности моего алгоритма, эти элементы(ниже) считаем отедльно
    # matrix[0][0] matrix[-1][0] matrix[0][-1] matrix[-1][-1]
    matrix_with_adjacent_zero = np.zeros((matrix.shape[0], matrix.shape[1]))
    for i in range(1, matrix.shape[0]-1):
        for j in range(1, matrix.shape[1]-1):
            if matrix[i][j] == 0:
                if matrix[i - 1][j] == 0:
                    matrix_with_adjacent_zero[i][j] += 1
                if matrix[i][j - 1] == 0:
                    matrix_with_adjacent_zero[i][j] += 1
                if matrix[i + 1][j] == 0:
                    matrix_with_adjacent_zero[i][j] += 1
                if matrix[i][j + 1] == 0:
                    matrix_with_adjacent_zero[i][j] += 1
    q = 0
    p = 0
    if matrix[q][p] == 0:
        if matrix[q][p + 1] == 0:
            matrix_with_adjacent_zero[q][p] += 1
        if matrix[q + 1][p] == 0:
            matrix_with_adjacent_zero[q][p] += 1
    q = 0
    p = -1
    if matrix[q][p] == 0:
        if matrix[q][p - 1] == 0:
            matrix_with_adjacent_zero[q][p] += 1
        if matrix[q + 1][p] == 0:
            matrix_with_adjacent_zero[q][p] += 1
    q = -1
    p = 0
    if matrix[q][p] == 0:
        if matrix[q][p + 1] == 0:
            matrix_with_adjacent_zero[q][p] += 1
        if matrix[q - 1][p] == 0:
            matrix_with_adjacent_zero[q][p] += 1
    q = -1
    p = -1
    if matrix[q][p] == 0:
        if matrix[q][p - 1] == 0:
            matrix_with_adjacent_zero[q][p] += 1
        if matrix[q - 1][p] == 0:
            matrix_with_adjacent_zero[q][p] += 1
    return matrix_with_adjacent_zero


def kill_lines_with_zero(matrix, matrix_zero):
    max_x = (0, -1)
    max_y = (0, -1)
    for i in range(matrix_zero.shape[0]):
        max_element = max(matrix_zero[i, :])
        if max_element > max_x[0]:
            max_x = (max_element, i)
    for j in range(matrix_zero.shape[1]):
        max_element = max(matrix_zero[:, j])
        if max_element > max_y[0]:
            max_y = (max_element, j)
    if max_x[0] > max_y[0]:
        matrix_copy = np.delete(matrix, max_x[1], 0)
        return kill_lines_with_zero(matrix_copy, calc_adjacent_zero(matrix))
    elif max_x[0] < max_y[0]:
        matrix_copy = np.delete(matrix, max_y[1], 1)
        return kill_lines_with_zero(matrix_copy, calc_adjacent_zero(matrix))
    elif max_x[0] == max_y[0] and max_x[0] > 0:
        matrix_copy = np.delete(matrix, max_x[1], 0)
        matrix_copy = np.delete(matrix, max_y[1], 1)
        return kill_lines_with_zero(matrix_copy, calc_adjacent_zero(matrix))
    else:
        # Дошло до сюда? Значит нет нулей рядом друг с другом.
        # Это хорошо, можно продолжать делить/зонировать
        return matrix


def hungarian_calc(matrix, a, b):
    if not check_zero(matrix):
        matrix = reduction_strings(matrix)
        matrix = reduction_columns(matrix)
        return hungarian_calc(matrix, a, b)

    return kill_lines_with_zero(matrix, calc_adjacent_zero(matrix))



test_matrix_two = np.array([
    [00, 1, 2, 3],
    [10, 11, 12, 13],
    [20, 21, 22, 23],
    [30, 31, 32, 33],
    [40, 41, 42, 43]
])


print(hungarian_calc(test_matrix, 0, 0))

# kek_lol = np.delete(test_matrix_two, 1, 1)
# print(kek_lol)
