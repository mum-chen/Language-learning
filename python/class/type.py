class Hello(object):
    def hello(self, name = 'word'):
        print('Hello, %s.' % name)

def fn(self, name = 'world'):
    print('Hello, %s.' % name)


Temp = type("Temp", (object,), dict(hello = fn))

if __name__ == '__main__':
    print(type(Hello))
    h = Hello()
    print(type(h))

    temp = Temp()
    temp.hello()
