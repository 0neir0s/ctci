#Given a positive integer, print the next smallest and the next largest number that have the same number of 1 bits in the binary representation

def getBinary(num):
    """ returns a binary array of the positive number """
    return bin(num)[2:]

def nextNumber(num):
    """ next bigger number with the same number of 1 bits """
    br = getBinary(num)
    length = len(br)
    c0 = length - 1 - br.rindex('1')
    c1 = length - 1 - br[:-c0].rindex('0')
    br[length-c0-c1-1] = 1
    br[length-c0-c1:] = [0]*(c0+c1)
    br[length -c1 + 1:] = [0]*max(0,c1-1)
    return br
