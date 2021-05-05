# Common bit tasks

def getBit(num, i):
    return (num & (1<<i)) != 0

def setBit(num, i):
    return num | (1<<i)

def clearBit(num, i):
    return num & ~(1<<i)

def clearBitsMSBthroughI(num, i):
    return num & ((1<<i)-1)

def clearBitsIthrough0(num, i):
    return num & (~0<<(i+1))

def updateBit(num, i, v):
    return (num & ~(1<<i)) | (v<<i)
