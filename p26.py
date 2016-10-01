def calcDecimal(numerator, denominator):
    remainder_set = {numerator}
    decimal = []
    while numerator != 0:
        while numerator <= denominator:
            numerator *= 10
            decimal.append(0)
        res = numerator / denominator
        numerator %= denominator
        numerator *= 10
        if numerator in remainder_set:
            break
        else:
            remainder_set.add(numerator)
            decimal.append(res)
    return decimal

max_dec = 1
result = 2
for i in xrange(2, 1000):
    dec = calcDecimal(1, i)
    if len(dec) > max_dec:
        max_dec = len(dec)
        result = i
print result
