import prime_util

prime100 = prime_util.generate_prime_list(100)

def get_signature(a, b):
    ret = ''
    for i, p in enumerate(prime100):
        si = 0
        while a != 1 and a % p == 0:
            si += 1
            a /= p
        ret += str(si*b) + '#'
    return ret

distinct = {''}
for a in xrange(2, 101):
    for b in xrange(2, 101):
        sig = get_signature(a, b)
        distinct.add(sig)
print len(distinct)-1
