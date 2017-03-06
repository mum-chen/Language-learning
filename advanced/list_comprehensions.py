L = range(1, 11)
print L


L = [x * x for x in range(1, 11)]
print L

L = [m + n for m in "ABC" for n in "XYZ"]
print L

d = {'x': 'A', 'y': 'B', 'z': 'C'}
L = [k + '=' + v for k, v in d.iteritems()]
print L

L = ['Hello', 'World', 18, 'Apple', None]
N = [s.lower() if isinstance(s, str) else s for s in L]
print N

N = [s.lower() for s in L if isinstance(s,str)]
print N
