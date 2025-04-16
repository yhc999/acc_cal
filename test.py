from accumulator import *

"""
下面所有的例子都会在前面给出一个要计算的序列和对应序列的通项公式, 计算的其实就是这个通项公式的n项积累,
积累方式可以是 + - * /
"""

# target: 1 + 2 + ... + n
# general formula: i
def sum_i(n):
    return accumulator(
        lambda i : i,
        add,
        0,
        n,
        1
    )
# test
# print(sum_i(3))
# print(sum_i(4))
# print(sum_i(10))
# print(sum_i(100))
# print(sum_i(1000))


# target : 1 + 2 + 4 + ... + 2^n
# general formula : 2^i
def sum_2i(n):
    return accumulator(
        lambda i : pow(2, i),   # item
        add,     # combine
        0,              
        n,
        0
    )
# test
# print(sum_2i(2)) # 1 + 2 + 4 = 7
# print(sum_2i(3)) # 1 + 2 + 4 + 8 = 15
# print(sum_2i(4)) # 31

# target : 0 + 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21 + ...(fibonacci)
def fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
def sum_fib(n):
    return accumulator(
        fib,
        add,
        0,
        n
    )
# test
# print(sum_fib(1))
# print(sum_fib(2))
# print(sum_fib(3))
# print(sum_fib(4))
