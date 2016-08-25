record = {1:1}

def collatz(x):
    if x not in record:
        if x % 2 == 0:
            c = 1 + collatz(x/2)
        else:
            c = 1 + collatz(x*3+1)
        record[x] = c
    return record[x]

max_step = 1
max_stater = 1
for i in xrange(2, 1000000):
    c = collatz(i)
    if max_step < c:
        max_step = c
        max_starter = i
print max_starter
