def fun(n):
    return lambda x: x * n

doubler = fun(2)
tripler = fun(3)

print(doubler(10))
print(tripler(10))