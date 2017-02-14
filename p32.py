pandigital = set()

def IsPandigital(a, b, c):
    sa = str(a)
    sb = str(b)
    sc = str(c)
    if ''.join(sorted(sa+sb+sc)) == '123456789':
        return True
    else:
        return False

for a in xrange(1, 10):
    for b in xrange(1234, 9877):
        c = a * b
        if IsPandigital(a, b, c):
            pandigital.add(c)

for a in xrange(12, 99):
    for b in xrange(123, 988):
        c = a * b
        if IsPandigital(a, b, c):
            pandigital.add(c)
print pandigital
print sum(pandigital)
