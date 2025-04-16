"""
通用积累器
item: procedure,用来计算第i项
combine: procedure,用来定义不同项之间结合的方式
start: 累积的初始值, 如果是相加累积为0, 相乘为1
n:  终止的项
i:  开始的项, 默认为0

example:

计算 1 + 2 + 3 + ... + n: 

def sum_i(n):
    return accumulator(
        lambda i : i,
        add,
        0,
        n,
        1
    )
"""
def accumulator(item, combine, start, n, i=0):
    acc = start
    while i <= n:
        val = item(i) #第i项的值
        acc = combine(acc, val)
        i += 1
    return acc

#+
def add(x, y):
    return x + y

#-
def sub(x, y):
    return x - y

#*
def mul(x, y):
    return x * y    

#/
def div(x, y):
    return x / y    

