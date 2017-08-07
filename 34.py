import math

def is_digf(x):
    origin = x
    s = 0
    while x > 0:
        d = x % 10
        x /= 10
        s += math.factorial(d)
    return origin == s

ret = 0
for i in range(10,2540160):
    if is_digf(i):
        ret += i
print ret
