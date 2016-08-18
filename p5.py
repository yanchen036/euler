prime_need = [1, 1, 1, 1, 1, 1, 1, 1]
prime = [2, 3, 5, 7, 11, 13, 17, 19]
elem = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]

def need(x):
    i = 0;
    ret = [0] * 8
    while x != 1:
        if x % prime[i] == 0:
            x /= prime[i]
            ret[i] += 1
        else:
            i += 1
    return ret 

def merge(a, b):
    ret = [0] * 8
    for i in xrange(8):
        ret[i] = max(a[i], b[i])
    return ret

for e in elem:
    pn = need(e)
    prime_need = merge(pn, prime_need)
res = 1
for i in xrange(8):
    for j in xrange(prime_need[i]):
        res *= prime[i]
print res
