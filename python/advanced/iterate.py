d = {'a': 1, 'b': 2, 'c': 3}

print "--"
for key in d:
    print key

print "--"
for value in d.itervalues():
    print value

print "--"
for k, v in d.iteritems():
    print k, v

print "--"
for ch in 'ABC':
    print ch

print "--"
for i, value in enumerate(['A', 'B', 'C']):
    print i, value

print "--"
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print x, y
