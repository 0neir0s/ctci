from functools import lru_cache

@lru_cache
def pathCount(x,y):
    if x==0 or y==0:
        return 1
    return pathCount(x-1,y) + pathCount(x,y-1)

def pathCountOL(matrix):
    """ Given the matrix of off-limits, find a path """
    @lru_cache
    def dfs(i,j):
        """ Give you a pass to X,Y from i,j if it exists """
        status = ( (i,j) == (X,Y)) or (
                   j+1<N and matrix[i][j+1] and dfs(i,j+1)) or (
                   i+1<M and matrix[i+1][j] and dfs(i+1,j))
        if status:
            path.append((i,j))
        return status

    M, N = len(matrix), len(matrix[0])
    X, Y = M-1, N-1
    path = []
    dfs(0,0)
    return path

print(pathCountOL([[1,0],[2,3]]))

def pathCounter(x,y):
    ''' Recursion with bottom up approach '''
    pathMap = {}
    for i in range(x+1):
        pathMap[(i,0)] = 1
    for j in range(y+1):
        pathMap[(0,j)] = 1
    for i in range(1,x+1):
        for j in range(1,y+1):
            pathMap[(i,j)] = pathMap[(i-1,j)] + pathMap[(i,j-1)]
    return pathMap[(x,y)]

print(pathCounter(4,5))
print(pathCounter(5,4))

# Alternatively, it is just choosing X 'R's and Y 'D's => (X+Y)C(X)
