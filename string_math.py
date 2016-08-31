def add(a, b):
    if len(a) < len(b):
        a, b = b, a
    carry = 0
    ret = ''
    a = a[::-1]
    b = b[::-1]
    len_a = len(a)
    len_b = len(b)
    for i in xrange(0, len_b):
        val = int(a[i]) + int(b[i]) + carry
        if val >= 10:
            carry = 1
            val -= 10
        else:
            carry = 0
        ret += str(val)
    for i in xrange(len_b, len_a):
        val = int(a[i]) + carry
        if val >= 10:
            carry = 1
            val -= 10
        else:
            carry = 0
        ret += str(val)
    if carry > 0:
        ret += '1' 
    return ret[::-1]

def mult(a, b):
    if len(a) > len(b):
        a, b = b, a
    ret = ''
    a = a[::-1]
    b = b[::-1]
    len_a = len(a)
    len_b = len(b)
    for i in xrange(0, len_a):
        prod = ''
        carry = 0
        ai = int(a[i])
        for j in xrange(0, len_b):
            val = carry + int(b[j]) * ai
            if val >= 10:
                carry = val / 10
                val %= 10
            else:
                carry = 0
            prod += str(val)
        if carry > 0:
            prod += str(carry)
        prod = prod[::-1]
        prod += '0'*i
        ret = add(ret, prod)
    return ret
