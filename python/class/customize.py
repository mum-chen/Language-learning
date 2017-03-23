class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__

    def __len__(self):
        return len(self.name)

    # same as lua mt.__index
    def __getattr__(self, attr):
        if attr == 'score':
            return 60
    def __call__(self):
        print self

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

if __name__ == '__main__':
    stu = Student("Mark")
    print stu, ",score:", stu.score
    if callable(stu):
        stu()

    print '----- __iter__ -----'
    for n in Fib():
        print n

    print '----- __getitem__ int '
    f = Fib()
    print f[20]

    print '----- __getitem__ slice '
    print f[:10]
