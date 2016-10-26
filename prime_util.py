def generate_prime_list(limit):
    prime_dict = [True] * limit
    prime_dict[0] = False
    prime_dict[1] = False
    prime_list = []
    for i in xrange(2, limit):
        if prime_dict[i]:
            prime_list.append(i)
            mult = 2
            while i*mult < limit:
                prime_dict[i*mult] = False
                mult += 1
    return prime_list
