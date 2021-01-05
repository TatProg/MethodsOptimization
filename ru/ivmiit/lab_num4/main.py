import numpy as np
import ru.ivmiit.lab_num4.op_plan_double_pred as op_double
import ru.ivmiit.lab_num4.op_plan_min_element as min_element

# Тестовые данные
# test_matrix = np.array([
#     [10, 20, 30, 40],
#     [100, 90, 80, 70],
#     [50, 15, 25, 60],
#     [95, 55, 25, 45]
# ])
# test_b = [1000, 1200, 1600, 2000]  # величина спроса
# test_a = [1600, 1000, 1200, 2000]  # объем производства
# test_n = 4

# Данные для лаб работы
lab_matrix = np.array([
    [3057, 3481, 3983],
    [2695, 3092, 3213],
    [3654, 3983, 4222]
])
lab_b = [1000, 1200, 1600]
lab_a = [1600, 1000, 1200]
lab_n = 3

# print(
#     op_double.find_op_plan(lab_matrix, lab_a, lab_b, lab_n)
# )
# -- op_double_pred --
# [[ 400.  600.    0.]
#  [1200.    0.    0.]
#  [   0.  400. 1200.]]

# print(
#     min_element.find_op_plan(lab_matrix, lab_b, lab_a, lab_n)
# )
# -- op_min_element --
# [[ 400.  600.    0.]
#  [1200.    0.    0.]
#  [   0.  400. 1200.]]
