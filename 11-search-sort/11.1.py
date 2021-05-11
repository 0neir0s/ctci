A = [0,9,10,11,13]
B = [1,4,7,10,12]

def merge(A,B):
    M, N = len(A), len(B)
    A.extend([0]*N)
    insertIndex, i, j = M+N-1, M-1, N-1

    while (i>=0) and (j>=0):
        if A[i] > B[j]:
            A[insertIndex] = A[i]
            i -= 1
        else:
            A[insertIndex] = B[j]
            j -= 1
        insertIndex -= 1
    if (j>=0):
        A[:j+1] = B[:j+1]

merge(A,B)
print(A)
