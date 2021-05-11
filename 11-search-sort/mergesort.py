def mergeSort(arr):
    """ return a sorted version of the array using merge sort """

    def merge(start, middle, end):
        """ merge 2 sorted arrays - [start to middle] and [middle to end] """
        L, R = arr[start:middle+1], arr[middle+1:end+1]
        lenL, lenR, i, j, k = len(L), len(R), 0, 0, start
        while i < lenL and j < lenR:
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        arr[k:end+1] = L[i:] if i<lenL else R[j:]
    
    def mergeSortFrom(start, end):
        if start >= end:
            return
        mid = (start+end)//2
        mergeSortFrom(start,mid)
        mergeSortFrom(mid+1,end)
        merge(start, mid, end)

    mergeSortFrom(0,len(arr)-1)

a = [1,2,4,3,8,5,6,2]
mergeSort(a)
print(a)
