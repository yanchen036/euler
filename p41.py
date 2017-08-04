import prime_util
from itertools import permutations

flag = False
for n in range(9,0,-1):
    a = [str(i) for i in range(n,0,-1)]
    for p in permutations(a):
        s = ''.join(p)
        d = int(s)
        if prime_util.is_prime(d):
            print d
            flag = True
            break
    if flag:
        break
