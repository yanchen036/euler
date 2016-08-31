import string_math

res = '1'
for f in xrange(2, 100):
    res = string_math.mult(res, str(f))
s = 0
print res
for d in res:
    s += int(d)
print s
