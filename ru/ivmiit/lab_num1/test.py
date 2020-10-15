import math as math

new_lower_bound = 22
new_upper_bound = 777
new_bound = -1

# print(new_lower_bound)
# print(new_upper_bound)
# print(new_bound)
#
# # new_bound, new_upper_bound, new_lower_bound = new_bound, new_lower_bound, new_upper_bound
# print()                 # x1=x3,  x2 =x1 ,  x3=x2
#
# new_lower_bound, new_upper_bound, new_bound = new_bound, new_lower_bound, new_upper_bound
#
# print(new_lower_bound)
# print(new_upper_bound)
# print(new_bound)


def f(x):
    return (x - 2) ** 2


def get_x_by_y(y):
    return math.sqrt(y)+2


def z(x1, x2):
    return 3*x1**2 + x2**2 - x1*x2 - 4*x1


print(f(22))
print(get_x_by_y(400))
print(z(-19, 8))

for i in range(2):
    for j in range(2):
        print(i)
        print(j)


