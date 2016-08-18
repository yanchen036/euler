def IsPalindromic(x):
    s = str(x)
    l = len(s)
    for i in xrange(l/2):
        if s[i] != s[-1-i]:
            return False
    return True

ma = 0
i = 999
while i >= 100:
    j = 999
    if i * j < ma:
        break
    while j >= i:
        res = i * j
        if IsPalindromic(res) and res > ma:
            ma = res
        j -= 1
    i -= 1
print ma
