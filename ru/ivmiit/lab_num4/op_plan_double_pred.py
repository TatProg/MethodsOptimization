import numpy as np

# Тестовые данные
# test_matrix = np.array([
#     [10, 20, 30, 40],
#     [100, 90, 80, 70],
#     [50, 15, 25, 60],
#     [95, 55, 25, 45]
# ])
# test_b = [1000, 1200, 1600, 2000]  # stroka, x, величина спроса
# test_a = [1600, 1000, 1200, 2000]  # stolbec, y, объем производства


# --- Формирование опорного плана методом двойного предпочтения ---
# Ищем наименьший элемент в строке(или в столбце) - отмечаем это
# Если он наименьший и там и тут, то "мега-отмечаем" его
# Все отметки в другой матрице, которую и возвращаем
# Для матриц больше 10х10, +=100 меняем на чет поболее, либо меняем логику
def double_trouble(main_matrix, n):
    m = n  # FIXME change NxN on NxM
    second_matrix = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            min_elem_stroka = min(main_matrix[i, :])
            index_min_elem_stroka = main_matrix[i, :].tolist().index(min_elem_stroka)
            min_elem_stolbec = min(main_matrix[:, j])
            index_min_elem_stolbec = main_matrix[:, j].tolist().index(min_elem_stolbec)

            if min_elem_stroka == min_elem_stolbec:
                second_matrix[index_min_elem_stolbec, index_min_elem_stroka] += 100
            else:
                second_matrix[i, index_min_elem_stroka] += 1
                second_matrix[index_min_elem_stolbec, j] += 1
    return second_matrix


# Пробегаемся по матрице из функции выше.
# Заполняем по алгоритму, сначала ** и тд
# Исключаем из дальнеше рассмотрения в рекурсивном цикле,
# путем замены уже ненужного числа на 10**10
# Дальше там дебильный костыль на проверку выхода, но я хз чо делать
def double_barrel(first_matrix, second_matrix, third_matrix, a, b, n):
    m = n  # FIXME change NxN on NxM
    # start to fill ** sections
    for i in range(n):
        for j in range(m):
            if second_matrix[i][j] > 100:
                if b[i] > a[j]:
                    b[i] -= a[j]
                    third_matrix[i][j] += a[j]
                    a[j] = 0
                    second_matrix[i][j] = 0
                    first_matrix[i][j] = 10 ** 10
                else:
                    a[j] -= b[i]
                    third_matrix[i][j] += b[i]
                    b[i] = 0
                    second_matrix[i][j] = 0
                    first_matrix[i][j] = 10 ** 10

    # start to fill * sections
    for i in range(n):
        for j in range(m):
            if second_matrix[i][j] > 0:
                # print("b[", j,"]=",b[j],"   a[",i,"]=",a[j] )
                if b[i] > a[j]:
                    b[i] -= a[j]
                    third_matrix[i][j] += a[j]
                    a[j] = 0
                    second_matrix[i][j] = 0
                    first_matrix[i][j] = 10 ** 10
                else:
                    a[j] -= b[i]
                    third_matrix[i][j] += b[i]
                    b[i] = 0
                    second_matrix[i][j] = 0
                    first_matrix[i][j] = 10 ** 10

    # start to fill other sections with recursion
    flag = check_all_zeros(a) * check_all_zeros(b)
    # if check_all_zeros(a) and check_all_zeros(b):  # FIXME what to do if ∑(a) != ∑(b)
    if flag:
        # окончание формирования опорного плана
        return third_matrix
    else:
        second_matrix = double_trouble(first_matrix, n)
        return double_barrel(first_matrix, second_matrix, third_matrix, a, b, n)


# np.nonzero и другие функции на проверку нулей или того,
# что все элементы равны друг другу (или нулю) - не работают.
# Вот костыль с flag'ом
def check_all_zeros(a):
    flag = True
    for i in range(len(a)):
        if a[i] != 0:
            flag = False
            return flag
    return flag


# Импортировать, а затем вызвать метод
def find_op_plan(test_matrix_1, a, b, n):
    test_matrix_2 = double_trouble(test_matrix_1, n)
    test_matrix_3 = np.zeros((n, n))
    final_matrix = double_barrel(test_matrix_1, test_matrix_2, test_matrix_3, a, b, n)
    return final_matrix
