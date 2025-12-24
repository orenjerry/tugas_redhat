def luar():
    return lambda a, b: a + b

f = luar()
print(f(4, 6))