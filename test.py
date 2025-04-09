from accumulator import accumulator

"""
下面所有的例子都会在前面给出一个要计算的序列和对应序列的通项公式, 计算的其实就是这个通项公式的n项积累,
积累方式可以是 + - * /
"""

# target: 1 + 2 + ... + n
# general formula: i
def sum_i(n):
    return accumulator(
        lambda i : i,
        lambda x,y : x + y,
        0,
        n,
        1
    )
# test
# print(sum_i(3))
# print(sum_i(10))
# print(sum_i(100))
# print(sum_i(1000))


# target : 1 + 2 + 4 + ... + 2^n
# general formula : 2^i
def sum_2i(n):
    return accumulator(
        lambda i : pow(2, i),   # item
        lambda x, y : x + y,     # combine
        0,              
        n,
        0
    )
# test
# print(sum_2i(2)) # 1 + 2 + 4 = 7
# print(sum_2i(3)) # 1 + 2 + 4 + 8 = 15
# print(sum_2i(4))


