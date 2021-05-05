from collections import defaultdict

lambda rnd = (x, rFigure=5): round(m, rFigure)

def lineKey(m, b):
    """ returns a key corresponding to this line """
    return rnd(m), rnd(b)

def computeMandB(p1, p2):
    """ returns the m,b version of the line going through p1 and p2
        for non-vertical lines, returns m, b
        for vertical lines, returns infinity, x-intercept """
    x1, y1 = p1
    x2, y2 = p2
    if rnd(x1) == rnd(x2):
        return inf,x2
    m = (y2-y1)/(x2-x1)
    b = y1 - m*x1
    return m, b

def bestLine(points):
    """ Given a list of points, finds the line with most number of points passing in it """
    lineMaps = defaultdict(int)
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            m, b = computeMandB(points[i], points[j])
            lineMaps[lineKey(m, b)] += 1
    return max(lineMaps, key = lambda k: lineMaps[k])
