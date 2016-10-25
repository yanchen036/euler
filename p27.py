prime_limit = 1000000
prime_dict = [True] * prime_limit
prime_dict[0] = False
prime_dict[1] = False
prime_list = []

for i in xrange(2, prime_limit):
    if prime_dict[i]:
        prime_list.append(i)
        mult = 2
        while i*mult < prime_limit:
            prime_dict[i*mult] = False
            mult += 1

maxa = maxb = maxn = 0
for a in xrange(-999,999):
    for b in xrange(-999,999):
        n = 0
        f = n*n + a*n + b
        while f > 1 and prime_dict[f]:
            n += 1
            f = n*n + a*n + b
        if n > maxn:
            maxn = n
            maxa = a
            maxb = b
print '%d %d %d' % (maxn, maxa, maxb)
