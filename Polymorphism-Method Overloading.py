class calc:
    def __init__(self):
        pass
    def total (self, a, b, c=0):
        return a + b + c

o = calc()

print(o.total(1,2))
print(o.total(1,2, 3))



