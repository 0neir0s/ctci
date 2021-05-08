from functools import cache

NEXT_DENOMINATOR = {25:10, 10:5, 5:1}

@cache
def waysNcents(n, denom=25):
    """ return the number of ways of representing n cents given unlimited number of quarters, dimes, nickels, pennies """
    if denom == 1:
        return 1
    ways, nextDenom = 0, NEXT_DENOMINATOR[denom]
    return sum([waysNcents(n-i, nextDenom) for i in range(0,n+1,denom)])

print(waysNcents(300))
