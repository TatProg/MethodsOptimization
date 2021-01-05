import numpy as np
import ru.ivmiit.lab_num4.op_plan_double_pred as op_double
import ru.ivmiit.lab_num4.op_plan_min_element as min_element

# Тестовые данные
test_matrix = np.array([
    [10, 20, 30, 40],
    [100, 90, 80, 70],
    [50, 15, 25, 60],
    [95, 55, 25, 45]
])
test_b = [1000, 1200, 1600, 2000]  # величина спроса
test_a = [1600, 1000, 1200, 2000]  # объем производства
test_n = 4

# print(
#     op_double.find_op_plan(test_matrix, test_a, test_b, test_n)
# )

# print(
#     min_element.find_op_plan(test_matrix, test_a, test_b, test_n)
# )

