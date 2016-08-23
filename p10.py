import math

prime = [2, 3]

def isPrime(x):
    sqr = int(math.sqrt(x))
    for pr in prime:
        if (pr > sqr):
            break
        if (x % pr == 0):
            return False
    return True

s = 5
for x in xrange(5, 2000000):
    if isPrime(x):
        prime.append(x)
        s += x
print s
