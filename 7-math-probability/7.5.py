# Square has lb and tr

class Square(object):
    def __init__(self, lb, side):
        self.lb = lb
        self.side = side

def lineCuttingInHalf(s1, s2):
    """ Cover the case where p1 and p2 are equal """
    x,y = s1.lb
    p1 = x+s1.side/2, y+s1.side/2
    x,y = s2.lb
    p2 = x+s2.side/2, y+s2.side/2
    if p1 == p2:
        return ((0,0), p1)
    return (p1, p2)
