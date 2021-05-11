
def interspersedSorted(arr, elem):
    """ Strings with empty strings interspersed """
    def interspersedSortedFrom(start, end):
        """ From start to end """
        if start > end:
            return False
        mid = (start+end)//2
        left, right = mid-1, mid+1
        while True:
            if left < start && right > end:
                return False
            if right <= end and arr[right]:
                mid = right
                break
            if left >= first and arr[left]:
                mid = left
                break
            left, right = left-1, right+1
        if arr[mid] == elem:
            return mid
        elif arr[mid] < elem:
            return interspersedSortedFrom(start, mid-1)
        else:
            return interspersedSortedFrom(mid+1, end)

    return interspersedSortedFrom(0, len(arr)-1)

