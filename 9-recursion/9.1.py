
def countWays(steps):
    ''' Recursion using bottom-up approach '''
    stepMap = { 1:1, 2:2, 3:4 }
    for i in range(4,steps+1):
        stepMap[i] = stepMap[i-1] + stepMap[i-2] + stepMap[i-3]
    return stepMap[steps]

print(countWays(4))
