# Given add and only add, define subtract, multiple, divide

def negate(n2):
    output, counter = 0, 0
    adder = 1 if n2 < 0 else -1
    while counter != a:
        output += adder
        counter += 1
    return output

def subtract(n1, n2):
    return n1 + negate(n2)

def multiplyPositive(n1, n2):
    output, counter = 0, 0
    while counter != n2:
        output += n1
        counter += 1
    return output

def multiply(n1, n2):
    if n2 < 0:
        n2 = negate(n2)
    return multiplyPositive(n1,n2)

def divide(n1, n2):
    sn1 = 1 if n1 > 0 else -1
    sn2 = 1 if n2 > 0 else -1
    pn1, pn2, sign = multiply(sn1,n1), multiply(sn2,n2), multiply(sn1,sn2)
    covered, q = 0, 0
    while not ((covered <= pn1) and ((covered+pn2) > pn1)):
        q += 1
        covered += n2
    if sign == 1:
        return (q, subtract(n1, covered))
    return (q+1, subtract(n2, subtract(n1, covered)))

