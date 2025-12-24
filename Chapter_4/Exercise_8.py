def luar(a, b):
    def dalam():
        return a + b
    return dalam


f = luar(5, 10)
print(f())