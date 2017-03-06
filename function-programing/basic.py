print '-------- basic '
f = abs

print f(-10)

def add(x, y, f):
    return f(x) + f(y)


def innerf(x):
    return x + 1

print add(1, 2, innerf)

print '-------- map/reduce'

