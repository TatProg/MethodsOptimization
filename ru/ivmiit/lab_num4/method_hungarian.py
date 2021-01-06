import numpy as np


# Тестовые данные
# test_matrix = np.array([
#     [10, 20, 30, 40],
#     [100, 90, 80, 70],
#     [50, 15, 25, 60],
#     [95, 55, 77, 45]
# ])


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
    for i in range(1, matrix.shape[0] - 1):
        for j in range(1, matrix.shape[1] - 1):
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
        return kill_lines_with_zero(matrix_copy, calc_adjacent_zero(matrix_copy))
    elif max_x[0] < max_y[0]:
        matrix_copy = np.delete(matrix, max_y[1], 1)
        return kill_lines_with_zero(matrix_copy, calc_adjacent_zero(matrix_copy))
    elif max_x[0] == max_y[0] and max_x[0] > 0:
        matrix_copy = np.delete(matrix, max_x[1], 0)
        matrix_copy = np.delete(matrix, max_y[1], 1)
        return kill_lines_with_zero(matrix_copy, calc_adjacent_zero(matrix_copy))
    else:
        # Дошло до сюда? Значит нет нулей рядом друг с другом.
        # Это хорошо, можно продолжать делить/зонировать, теперь уже учтем тот факт,
        # что при вычеркивании строки/столбца должны вычеркнуть как можно меньше элементов
        return matrix


def count_zeros_in_lines(matrix):
    matrix_with_only_zero = np.zeros((matrix.shape[0], matrix.shape[1]))
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i][j] == 0:
                matrix_with_only_zero[i][j] += 1
    zeros_in_line = []
    for i in range(matrix_with_only_zero.shape[0]):
        zero_count_in_line = sum(matrix_with_only_zero[i, :])
        zeros_in_line.append(zero_count_in_line)
    return zeros_in_line


def count_zeros_in_columns(matrix):
    matrix_with_only_zero = np.zeros((matrix.shape[0], matrix.shape[1]))
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i][j] == 0:
                matrix_with_only_zero[i][j] += 1
    zeros_in_column = []
    for j in range(matrix_with_only_zero.shape[1]):
        zero_count_in_column = sum(matrix_with_only_zero[:, j])
        zeros_in_column.append(zero_count_in_column)
    return zeros_in_column


def kill_lines_accuratly(matrix):
    zeros_in_line = count_zeros_in_lines(matrix)
    zeros_in_column = count_zeros_in_columns(matrix)
    if max(zeros_in_line) > max(zeros_in_column) > 1:
        matrix_copy = np.delete(matrix, zeros_in_line.index(max(zeros_in_line)), 0)
        print("X ось", zeros_in_line.index(max(zeros_in_line)))
        return kill_lines_accuratly(matrix_copy)
    elif max(zeros_in_column) > max(zeros_in_line) > 1:
        matrix_copy = np.delete(matrix, zeros_in_column.index(max(zeros_in_column)), 1)
        print("Y ось", zeros_in_column.index(max(zeros_in_column)))
        return kill_lines_accuratly(matrix_copy)
    elif (max(zeros_in_line) == max(zeros_in_column)) and (max(zeros_in_column) > 1):
        matrix_copy = np.delete(matrix, zeros_in_line.index(max(zeros_in_line)), 0)
        matrix_copy = np.delete(matrix, zeros_in_column.index(max(zeros_in_column)), 1)
        print("X ось", zeros_in_line.index(max(zeros_in_line)))
        print("Y ось", zeros_in_column.index(max(zeros_in_column)))
        return kill_lines_accuratly(matrix_copy)
    else:
        new_matrix = kill_last_zero(matrix)
        # осталось слишком мало нулей, сокращаем последний, если есть и
        # можно начинать вычитать и прибавлять
        return new_matrix


def kill_last_zero(matrix):
    zeros_in_line = count_zeros_in_lines(matrix)
    zeros_in_column = count_zeros_in_columns(matrix)

    # # Костыль на случай конфликта типов
    # if not isinstance(zil, list):
    #     zeros_in_line = zil.tolist()
    # else:
    #     zeros_in_line = zil
    # if not isinstance(zic, list):
    #     zeros_in_column = zic.tolist()
    # else:
    #     zeros_in_column = zic

    if max(zeros_in_line) == 0 or max(zeros_in_column) == 0:
        return matrix  # Если нулей не осталось, то можно выходить, начинать вычитать и прибавлять
    if max(zeros_in_line) > max(zeros_in_column):
        delete_index = zeros_in_line.index(max(zeros_in_line))
        new_matrix = np.delete(matrix, delete_index, 0)
        return kill_last_zero(new_matrix)
    elif max(zeros_in_line) < max(zeros_in_column):
        delete_index = zeros_in_column.index(max(zeros_in_column))
        new_matrix = np.delete(matrix, delete_index, 1)
        return kill_last_zero(new_matrix)
    elif max(zeros_in_line) == max(zeros_in_column):
        # костыль.
        if matrix.shape[0] > matrix.shape[1]:
            delete_index = zeros_in_line.index(max(zeros_in_line))
            new_matrix = np.delete(matrix, delete_index, 0)
            return kill_last_zero(new_matrix)
        else:
            delete_index = zeros_in_column.index(max(zeros_in_column))
            new_matrix = np.delete(matrix, delete_index, 1)
            return kill_last_zero(new_matrix)
        # delete_index_1 = zeros_in_line.index(max(zeros_in_line))
        # delete_index_2 = zeros_in_column.index(max(zeros_in_column))
        # new_zero_in_line = np.delete(zeros_in_line, delete_index_1)
        # new_zero_in_column = np.delete(zeros_in_line, delete_index_2)
        # new_matrix = np.delete(matrix, delete_index_1, 1)  # or delete_index_2, whatever
        # return kill_last_zero(new_matrix, new_zero_in_line, new_zero_in_column)
    else:
        return matrix


def hungarian_calc(matrix):
    if not check_zero(matrix):
        matrix = reduction_strings(matrix)
        matrix = reduction_columns(matrix)
        return hungarian_calc(matrix)
    # print(matrix)
    new_matrix = kill_lines_with_zero(matrix, calc_adjacent_zero(matrix))
    new_matrix = kill_lines_accuratly(new_matrix)
    # print(new_matrix)
    # последний шаг:
    min_elem = new_matrix.min()
    last_matrix = new_matrix - min_elem
    # print(last_matrix)
    # Костыль. Делаем замену:
    for q in range(new_matrix.shape[0]):
        for p in range(new_matrix.shape[1]):
            for i in range(matrix.shape[0]):
                for j in range(matrix.shape[1]):
                    if new_matrix[q][p] == matrix[i][j]:
                        matrix[i][j] = last_matrix[q][p]
    # fill_table(matrix)
    return matrix


# def fill_table(matrix):
#     filled_matrix = np.zeros((matrix.shape[0], matrix.shape[1]))
#     lab_b = [1000, 1200, 1600]
#     lab_a = [1600, 1000, 1200]
#     zil = count_zeros_in_lines(matrix)
#     zic = count_zeros_in_columns(matrix)
#     if zil.min() == 1:
#         index_zil = zil.index(1.0)
#         for j in range((matrix.shape[1]):
#             if matrix[index_zil][j]

