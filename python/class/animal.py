class Animal(object):
    def move(self):
        print 'Animal is running ...'


class Dog(Animal):
#   It also rewrite the system variable
    def __len__(self):
        return 4

class Cat(Animal):
    pass

class Bird(Animal):
    def move(self):
        print 'Bird is flying ...'

class FakeAnimal(object):
    def move(self):
        print 'Fake animal is static!'



def move_twice(animal):
    animal.move()
    animal.move()

if __name__ == '__main__':
    dog = Dog()
    cat = Cat()

    dog.move()
    cat.move()

    bird = Bird()
    bird.move()

    print "--------- move twice --------------------"
    move_twice(bird)
    move_twice(dog)

#   this is duck-type
    move_twice(FakeAnimal())


    print "--------- some fun ----------------------"
    print 'How many legs dog has:', len(dog)

    print 'If dog is Animal:', isinstance(dog, Dog)
    move = getattr(dog, 'move', 404)
    move()

    print "--------- dir/isinstance/type ------------"
    print(type(dog))
    print dir(dog)

