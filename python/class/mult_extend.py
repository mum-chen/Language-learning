class Movable(object):
    def move(self):
        print "Moving"

class Runnable(object):
    def run(self):
        print 'Running ...'
    
    def move(self):
        self.run()

class Flyable(object):
    def fly(self):
        print 'Flying'

    def move(self):
        self.fly()

class Animal(object):
    def kind(self):
        print "I'm", getattr(self, '_kind', "Animal")

class Mammal(Animal):
    def __init__(self):
        self._kind = "Mammal"

class Bird(Animal):
    def __init__(self):
        self._kind = "Bird"

class Dog(Mammal, Runnable):
    pass

class Bat(Mammal, Flyable):
    pass

class Parrot(Bird, Flyable):
    pass

class Ostrich(Bird, Runnable):
    pass

def introduce(movable_animal):
    movable_animal.kind()
    movable_animal.move()


if __name__ == '__main__':
    dog = Dog()
    bat = Bat()
    parrot = Parrot()
    ostrich = Ostrich()

    print '--- first --'
    introduce(dog)
    print '--- next ---'
    introduce(bat)
    print '--- next ---'
    introduce(parrot)
    print '--- next ---'
    introduce(ostrich)
