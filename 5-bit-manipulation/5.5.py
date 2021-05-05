def bitSwapAtoB(a, b):
    """ return the number of bit swaps needed to change from a to b """
    return bin(a^b).count('1')

def pureBitSwapAtoB(a, b):
    c, count = a^b, 0
    while c:
        c = c & (c-1) #Clears the least significant digit
        count++
    return count
