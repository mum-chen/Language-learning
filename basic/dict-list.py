d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print d['Michael']

d['Jack'] = 90
print d['Jack']


# error with call empty index
# print d['Thomas']

# check the key
print 'Thomas' in d

print d.get('Thomas')
print d.get('Thomas', -1)

d.pop('Bob')
print d
# the key must an invariable

print '------ set ---------------'
s = set([1, 2, 3, 1])
print s
s.add(4)
s.add(4)
print s
s.remove(4)
print s

s1 = set([5, 2, 6])

print r'-- &'
print s1 & s
print r'-- |'
print s1 | s
