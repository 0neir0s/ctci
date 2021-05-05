def insertInto(N, M, i, j):
    """ insert M into N such that M starts at bit j and ends at bit i """
    clearMask = ((1 << (j+1))-1) & (~0 << i)
    print(bin(clearMask))
    return (N & clearMask) | (M << i)

print(insertInto(10000000000,10011,2,6))
