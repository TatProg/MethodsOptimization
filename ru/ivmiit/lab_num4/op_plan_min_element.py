import numpy as np

# Тестовые данные
test_matrix = np.array([
    [10, 20, 30, 40],
    [100, 90, 80, 70],
    [50, 15, 25, 60],
    [95, 55, 35, 45]
])

test_b = [1000, 1200, 1600, 2000]  # stroka, x, величина спроса
test_a = [1600, 1000, 1200, 2000]  # stolbec, y, объем производства
test_n = 4


# --- Формирование опорного плана методом минимального элемента ---
# Алгоритм простой - нашли минимум в матрице, сделали вычет а из б (или б из а),
# если получили ноль, то убрали строку и/или столбик, и так до конца
def form_plan(matrix_1, matrix_2, a, b, n):
    m = n  # FIXME change NxN on NxM
    index = find_index_of_min_elem_in_matrix(matrix_1, n)
    str = index[0]
    col = index[1]
    if b[col] > a[str]:
        b[col] -= a[str]
        matrix_2[str][col] += a[str]
        a[str] = 0
        matrix_1 = kill_line_x(matrix_1, str, n)
        matrix_1[str][col] = 111111
    elif b[col] < a[str]:
        a[str] -= b[col]
        matrix_2[str][col] += b[col]
        b[col] = 0
        matrix_1 = kill_line_y(matrix_1, col, n)
        matrix_1[str][col] = 444444
    elif b[col] == a[str] and (b[col] != 0 or a[str] != 0):  # Костыль какой-то
        matrix_2[str][col] += b[col]
        a[str] -= b[col]
        b[col] = 0
        # print("a = ", a[j], "   b = ", b[i])
        matrix_1 = kill_line_x(matrix_1, str, n)
        matrix_1 = kill_line_y(matrix_1, col, n)
        matrix_1[str][col] = 555555
    # else:
    #     return None
    flag = check_all_zeros(a) * check_all_zeros(b)
    # if check_all_zeros(a) and check_all_zeros(b):  # FIXME what to do if ∑(a) != ∑(b)
    if flag:
        # окончание формирования опорного плана
        return matrix_2
    else:
        return form_plan(matrix_1, matrix_2, a, b, n)


def kill_line_x(matrix, x, n):
    for j in range(n):
        matrix[x][j] = 777777
    return matrix


def kill_line_y(matrix, y, m):
    for i in range(m):
        matrix[i][y] = 888888
    return matrix


# Копия костыля из Двойных предпочтений для проверки нулей в a и b
def check_all_zeros(a):
    flag = True
    for i in range(len(a)):
        if a[i] != 0:
            flag = False
            return flag
    return flag


def find_index_of_min_elem_in_matrix(matrix, n):
    m = n  # FIXME change NxN on NxM
    min_element = matrix[0][0]
    index = (0, 0)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] < min_element:
                min_element = matrix[i][j]
                index = (i, j)
    return index


# Импортировать, а затем вызвать метод
def find_op_plan(matrix_1, a, b, n):
    matrix_2 = np.zeros((n, n))
    final_matrix = form_plan(matrix_1, matrix_2, a, b, n)
    return final_matrix
