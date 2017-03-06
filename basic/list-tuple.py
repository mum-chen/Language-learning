# -*- coding: utf-8 -*-
print "-------------- py list -----------------"
classmates = ["AA", "BB", "CC"]
print classmates, len(classmates)

# begin with 0
print classmates[0]
# also input a negtaive number
print classmates[-1]

classmates.append("DD")
print classmates, len(classmates)

classmates.insert(1, "AA1")
print classmates, len(classmates)

classmates.pop(1)
print classmates, len(classmates)

classmates[1] = "BB1"
print classmates, len(classmates)


print "-------------- py tuple ----------------"
animals = ("cat", "dog")
print animals, len(animals)

# number
t = (1)
# tuple
t = (1,)
