from math import ceil

def swapOddEvenbits(a):
    """ Swap even and odd bits with as few instructions as possible """
    l = ceil(len(bin(a)[2:])/2)
    evenMask, oddMask = int('10'*l,2), int('01'*l,2)
    return ((a & evenMask) >> 1) | ((a & oddMask) << 1)

print(swapOddEvenbits(4))
