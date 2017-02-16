from fractions import Fraction

def Simplify(a, b):
    sa = str(a)
    sb = str(b)
    common = set(sa).intersection(sb) 
    if sa[0] in common:
        na = sa[1]
    else:
        na = sa[0]
    if sb[0] in common:
        nb = sb[1]
    else:
        nb = sb[0]
    return int(na), int(nb) 
        
prod = Fraction(1,1)
for i in xrange(11, 99):
    for j in xrange(i+1, 100):
        si = str(i)
        sj = str(j)
        if si[1] == sj[0] and sj[1] != '0':
            f1 = Fraction(i, j)
            f2 = Fraction(int(si[0]), int(sj[1]))
            if f1 == f2:
                prod *= f1
print prod

