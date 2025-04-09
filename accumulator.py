"""
通用积累器
item: procedure,用来计算第i项
combine: procedure,用来定义不同项之间结合的方式
k: 起始值
n: i的最终值
start: i的初始值,也就是从第几项开始计算

example:

计算 1 + 2 + 3 + ... + n: 

常规写法:
define item(i):
    return i
define combine(x, y):
    return x + y
define sum_i(n):
    return accumulator(item, combine, 0, n, 1)

lambda版本(语法糖,更加简洁):
def sum_i(n):
    return accumulator(
        lambda i : i,
        lambda x,y : x + y,
        0,
        n,
        1
    )
"""
def accumulator(item, combine, k, n, start):
    i = start
    while i <= n:
        val = item(i) #第i项的值
        k = combine(k, val)
        i += 1
    return k
