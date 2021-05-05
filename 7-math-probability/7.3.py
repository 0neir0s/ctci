# Choose the simplest data-structure which is needed - in this case, it can be a tuple (m,b) representing y = mx+b

from math import abs

def fEquals(f1, f2, epsilon=0.001):
    return abs(f1 - f2) < epsilon

def intersect (l1, l2):
    """ Check if l1 and l2 intersects """
    m1, b1 = l1
    m2, b2 = l2
    return (not fEquals(m1,m2)) || fEquals(b1,b2)
