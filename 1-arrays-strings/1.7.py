def zeroTransform (matrix):
    ''' an MxN matrix - if an element in it is 0, its entire row and column are to be set to 0 '''
    M,N, rows, cols = len(matrix), len(matrix[0]), set(), set()
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
    for i in range(M):
        for j in range(N):
            if i in rows or j in cols:
                matrix[i][j] = 0
    return matrix

print(zeroTransform([[1,2,0],[4,5,6],[7,0,9]]))
