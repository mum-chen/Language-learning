print '-------- basic '
f = abs

print f(-10)

def add(x, y, f):
    return f(x) + f(y)


def innerf(x):
    return x + 1

print add(1, 2, innerf)

print '-------- map'
def f(x):
    return x * x

L = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print L

def add(x, y):
    return x + y

print '-------- reduce'
L = reduce(add, range(10))
print L


def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

print str2int("12345")


print '-------- filter'
def is_odd(n):
    return n % 2 == 1
print filter(is_odd, range(10))

print '-------- sorted'
L = [21, 18, 23, 03, 43, 51]
print sorted(L)

def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0

print sorted(L, reversed_cmp)


