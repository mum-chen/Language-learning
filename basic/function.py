def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


def empty():
    pass

print my_abs(-10)
empty()

def my_abs_full(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    return my_abs(x)

# my_abs_full("A")
print my_abs_full(98)

def mult_valut():
    return 1, 2

# the return value is a tuple
print mult_valut()


print '--------- default value --------'
def power(x):
    return x * x

print power(5)

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# call an error
# print power(5)

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print power(5)
print power(5, 3)

print '----------- some trap in default value '
def add_end(L=[]):
    L.append('END')
    return L

print "-- error default value"
print add_end()
print add_end()

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print add_end()
print add_end()

print '----------- varying parameter'
def calc(numbers):
    s = 0
    for n in numbers:
        s = s + n * n
    return s

print calc([1, 3, 5, 7])
# error
# print calc(1, 3, 5, 7)

def calc(*numbers):
    s = 0
    for n in numbers:
        s = s + n * n
    return s

# error
# print calc([1, 3, 5, 7])
print calc(1, 3, 5, 7)

nums = [1, 2, 3]
print calc(*nums)

# call a tuple or a list to varying parameter

print '----------- four type of input'
def func(a, b, c=0, *arg, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', arg, 'kw =', kw

func(1, 2)
func(1, 2, 3)
func(1, 2, 3, 'a', 'b')
func(1, 2, 3, 'a', 'b', x=99)

args = (1, 2, 3, 4)
kw = {'x': 99, 'y': 100}
func(*args, **kw)
# for every function, it accept func(*args, **kw)
