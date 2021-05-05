from collections import deque

def kthFactorV1(k):
    """ find the kth number (0 index) whose only prime factors are 3,5,7
        Time complexity of O(k^2) """
    a,b,c = 3,5,7
    factors = {1,3,5,7}
    if k<4:
        return factors[k]
    for i in range(4,k+1):
        nxt = inf
        for f in factors:
            nxt = min(nxt, min([i for i in [f*a, f*b, f*c] if i not in factors])
        factors.add(nxt)
    return max(factors)

def removeMin(q):
    """ Remove minimum value and all its instances from q """
    val = min(q)
    for _ in range(q.count(val)):
        q.remove(val)
    return val

def kthFactorV2(k):
    """ find the kth number (0 index) whose only prime factors are 3,5,7
        Better than previous one. Instead of generating the next, push the possible ones in the queue """
    val, q = 1, deque([3,5,7])
    for _ in range(k):
        val = removeMin(q)
        q.extend([val*3, val*5, val*7])
    return val

def kthFactor(k):
    """ Optimised version - not adding duplicate entries at all """
    val, q3, q5, q7 = 1, deque([3]), deque([5]), deque([7])
    for _ in range(k):
        minQ = min([q3,q5,q7], key=lambda x: x[0])
        val = minQ.popleft()
        if minQ == q3:
            q3.append(val*3)
            q5.append(val*5)
        elif minQ == q5:
            q5.append(val*5)
        q7.append(val*7)
    return val
