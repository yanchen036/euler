# a+b+c = 1000
# a^2+b^2=c^2 -> -ab+1000a+1000b = 500000
# a+b>c -> a+b>500
# c>a -> 1000-b>2a
# c>b -> 1000-a>2b
for a in xrange(1, 500):
    for b in xrange(500-a+1, 500):
        if 1000-b > 2*a and 1000-a > 2*b and -1*a*b + 1000*a + 1000*b == 500000:
            print('%d %d %d' % (a, b, 1000-a-b))
            print a*b*(1000-a-b)
