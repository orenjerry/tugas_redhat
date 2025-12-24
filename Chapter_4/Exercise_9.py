def luar():
    def dalam(a, b):
        return a + b
    return dalam


f = luar()
print(f(3, 7))