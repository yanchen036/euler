def divsorNum(x):
    ret = 1
    i = 2
    bound = x
    while i < bound:
        if  x % i == 0:
            ret += 2
            bound = x / i
        i += 1
    return ret

s = 0
i = 1
while True:
    s += i
    i += 1
    dn = divsorNum(s)
    if dn >= 500:
        print s
        break
