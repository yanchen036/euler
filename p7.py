import math

def isPrime(x):
    sqr = int(math.sqrt(x))
    for pr in prime:
        if (pr > sqr):
            break
        if (x % pr == 0):
            return False
    return True

prime = [2, 3]
i = 5
while len(prime) < 10001:
    if isPrime(i):
        prime.append(i)
    i += 1
print prime[-1]
