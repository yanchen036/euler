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

target = 600851475143
tsqr = int(math.sqrt(target))
cur = 5
while (cur <= tsqr):
    if (isPrime(cur)):
        prime.append(cur)
    cur += 1

factor = []
for p in prime:
    if (target % p == 0):
        factor.append(p)
print factor[-1]

