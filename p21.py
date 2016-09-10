import threading

def divisor(x):
    div = []
    for i in xrange(1, x/2+1):
        if x % i == 0:
            div.append(i)
    return div

def compSumHelper(idx, div, cur_sum, comp_sum):
    if cur_sum >= 10000:
        return
    if idx == len(div):
        if cur_sum != 0:
            comp_sum.add(cur_sum)
    else:
        compSumHelper(idx+1, div, cur_sum+div[idx], comp_sum)
        compSumHelper(idx+1, div, cur_sum, comp_sum)

def compSum(div):
    comp_sum = set()
    compSumHelper(0, div, 0, comp_sum)
    return comp_sum

bound = 1000
thread_num = 10
n2sum = {}
def i2sum(starter):
    for i in xrange(starter, bound, thread_num):
        print '2sum %d' % i
        div = divisor(i)
        sum_set = compSum(div)
        n2sum[i] = sum_set

class myThread(threading.Thread):
    def __init__(self, threadID, starter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.starter = starter
    def run(self):
        i2sum(self.starter)
        print 'Exiting %d' % self.threadID

thread_list = []
for i in xrange(thread_num):
    thread = myThread(i, i+1)
    thread.start()
    thread_list.append(thread)
for t in thread_list:
    t.join()

print 'finish'

#amicable = set()
#for a in xrange(2, bound):
#    print 'process %d' % i
#    for b in n2sum[a]:
#        if a != b and a in n2sum[b]:
#            amicable.add(a)
#            amicable.add(b)
#ami_sum = 0
#for s in amicable:
#    ami_sum += s
#print ami_sum
