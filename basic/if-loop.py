age = 10

if age > 1:
    print "your age is", age
elif age > 18:
    print "your age is", age
    print "adult"
else:
    print "infant"


# False, 0, '', empty-list

print "----------- loop ----------------"
names = ["AA", "BB", "CC", "DD"]

for name in names:
    print name

# from 0-4
print range(5)


s = 0
n = 99
while n > 0:
    s = s + n
    n = n -2
print s

birth = raw_input('birth: ')
birth = int(birth)
if birth < 2000:
    print 'before 00'
else:
    print 'after 00'
