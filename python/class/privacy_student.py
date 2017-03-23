
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)


if __name__ == '__main__':
    bart = Student('bart simpson', 59)
    lisa = Student('lisa simpson', 87)
    bart.print_score()
    lisa.print_score()

#   interpreter change the __xxx to _ClassName__xxx
    print bart._Student__name   # success
    print bart.__name           # error
