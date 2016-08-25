def mult2(x):
    carry = 0
    ret = ''
    x = x[::-1]
    for i in xrange(0, len(x)):
        val = carry + int(x[i])*2
        if val >= 10:
            val -= 10
            carry = 1
        else:
            carry = 0
        ret += str(val)
    if carry > 0:
        ret += '1'
    return ret[::-1]

v = '1'
for p in xrange(1, 1001):
    v = mult2(v)
s = 0
for e in v:
    s += int(e)
print s
