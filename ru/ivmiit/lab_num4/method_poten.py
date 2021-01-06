import numpy as np


def check_method(matrix, a, b, n):
    m = n  # FIXME change NxN on NxM
    if sum(a) == sum(b):
        print("Open. ∑a == ∑b")
    else:
        print("Close. ∑a != ∑b")

    cell_check = m * n
    for i in range(n):
        for j in range(m):
            if matrix[i][j] > 0:
                cell_check -= 1
    if cell_check == (m + n - 1):
        print("Good ", cell_check)
    else:
        print("Bad. ", cell_check)


# --- Вычисление потенциалов для плана перевозки ---
# def potential_calc(matrix, a, b, n): # todo this method
