
class Animal(object):
    def eat(self):
        print('Animal eating')

class EatableMixin(object):
    def eat(self):
        print("EatableMixin eating")

class Cat(Animal, EatableMixin):
    pass

class Dog(EatableMixin, Animal):
    pass

if __name__ == '__main__':
    # mult class will extend the first method
    cat = Cat()
    cat.eat()

    dog = Dog()
    dog.eat()
