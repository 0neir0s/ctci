def magicIndex(arr):
    """ return the index which satisfies arr[i] = i """

    def bs(start, end):
        """ Modified binary search """
        if not (0 <= start <= end < N): 
            return -1
        mid = (start + end)//2
        if arr[mid] == mid:
            return mid
        if arr[mid] > mid:
            return bs(start, mid-1)
        return bs(mid+1, end)

    N = len(arr)
    return bs(0, N-1)

def magicIndexRepeating(arr):
    """ support non-distinct sorted array """
    
    def bs(start, end):
        """ Modified binary search """
        if not (0 <= start <= end < N):
            return -1
        mid = (start + end)//2
        if arr[mid] == mid:
            return mid
        if arr[mid] > mid:
            output = bs(arr[mid], end)
            if output != -1:
                return output
            return bs(start, mid-1)
        output = bs(start, arr[mid])
        if output != -1:
            return output
        return bs(mid+1, end)
    
    N = len(arr)
    return bs(0,N-1)

print(magicIndex([-13,-7,-6,-3,0,1,2,3,5,9,11,12]))
print(magicIndexRepeating([-13,-7,-6,-3,0,1,2,3,5,9,11,12]))
