a = ['0000','0001','0010','0011','0101','0110','0111']

def missingInteger(a):
    """ find the missing integer given the binary list of elem """
    checker = ''.join( [i[-1] for i in a] )
    return (checker.find('11')+1) or (checker.find('00')+1)

print(missingInteger(a))
