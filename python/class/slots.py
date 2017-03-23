from types import MethodType

class Student(object):
    
    __slots__ = ('name', 'age', 'score', 'set_age', 'set_score')

    def introduce(self):
        name = getattr(self, 'name', 'student')
        print "I'm", name

def set_age(self, age):
    self.age = age

def set_score(self, score):
    self.score = score

if __name__ == '__main__':
#   set attr dynamic
    s = Student()
    s.introduce()
    s.name = 'Michael'
    s.introduce()

#   set method dynamic(for single instance)
    s.set_age = MethodType(set_age, s, Student)
    s.set_age(25)

    # cause error
    # Student().set_age(23)

    Student.set_score = MethodType(set_score, None, Student)
    s.set_score(100)
    s2 = Student()
    s2.set_score(99)
    print s.score, s2.score

    # cause error
    # s.aaa = 10
