def divisorSum(x):
    div_sum = 0
    for i in xrange(1, x/2+1):
        if x % i == 0:
            div_sum += i
    return div_sum

bound = 10000
divsor_sum = [0] * (bound+1)
for i in xrange(2, bound):
    ds = divisorSum(i)
    divsor_sum[i] = ds

amicable = set()
for a in xrange(2, bound):
    b = divsor_sum[a]
    if b > 0 and b < bound and a != b and divsor_sum[b] == a:
        amicable.add(a)
        amicable.add(b)
ami_sum = 0
for s in amicable:
    ami_sum += s
print ami_sum
