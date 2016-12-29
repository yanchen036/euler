import math

# 9^5*6 = 354294
# only consider numbers < 354294

def FifthPowSum(x):
    s = 0
    while x > 0:
        digit = x % 10
        s += math.pow(digit, 5)
        x /= 10
    return s

s = 0
for i in xrange(2, 354294):
    if i == FifthPowSum(i):
        s += i
        print 'find %d' % i
print s
