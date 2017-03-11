print ' gen with compre '
L = [x * x for x in range(10)]
print L

g = (x * x for x in range(10))
print g

for n in g:
    print n

print ' gen with function '
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # case next yield
        yield b
        a, b = b, a + b
        n = n + 1

for n in fib(6):
    print n
