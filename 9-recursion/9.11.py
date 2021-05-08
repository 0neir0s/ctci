def numberOfWays(expr, value):
    """ No of distinct ways of parenthesising the expression such that its value is the given value """
    VALUES = {'0': False, '1': True}

    def numberOfWaysSubExp(value, start, end):
        """ return the possibilities of sub-expression from start to end returns value """
        if expr[start:end] in VALUES:
            return int(VALUES[expr[start:end]] == value)
        total = 0
        for i in range(start, end):
            if expr[i] == '&':
                if value:
                    total += numberOfWaysSubExp(True, start, i) * numberOfWaysSubExp(True, i+1, end)
                else:
                    total += numberOfWaysSubExp(True, start, i) * numberOfWaysSubExp(False, i+1, end) + numberOfWaysSubExp(False, start, i) * numberOfWaysSubExp(True, i+1, end)
            if expr[i] == '|':
                if value:
                    total += numberOfWaysSubExp(True, start, i) * numberOfWaysSubExp(False, i+1, end) + numberOfWaysSubExp(True, start, i) * numberOfWaysSubExp(True, i+1, end) + numberOfWaysSubExp(False, start, i) * numberOfWaysSubExp(True, i+1, end)
                else:
                    total += numberOfWaysSubExp(False, start, i)*numberOfWaysSubExp(False, i+1, end)
        return total
    N = len(expr)
    return numberOfWaysSubExp(value, 0, N)


print(numberOfWays( '1&0|1|1', False))
print(numberOfWays( '1&0|1|1', True))

