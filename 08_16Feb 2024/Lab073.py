import math


def sq_rt(num):
    return math.sqrt(num)


list1 = [21, 25, 54]
sqrt_list = list(map(sq_rt, list1))
print(sqrt_list)
