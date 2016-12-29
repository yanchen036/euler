coins = [200, 100, 50, 20, 10, 5, 2, 1]

def recurrent(total, cur_coin, succ):
    if total == 200:
        succ[0] += 1
        return
    else:
        while cur_coin < 7:
            if total + coins[cur_coin] <= 200:
                recurrent(total + coins[cur_coin], cur_coin, succ)
            cur_coin += 1

ret = [0]
recurrent(0, 0, ret)
print ret[0]
