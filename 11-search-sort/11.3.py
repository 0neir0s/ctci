def searchInRotated(arr, elem):
    """ search in an array rotated unknown number of times """
    def searchInRotatedFrom(start, end):
        """ search in a subsection """
        if start > end:
            return False
        mid = (start+end)//2
        val = arr[mid]
        if val == elem:
            return True
        if arr[start] < arr[mid]:
            if arr[start] <= val <= arr[mid]:
                return searchInRotatedFrom(start,mid-1)
            else:
                return searchInRotatedFrom(mid+1, end)
        elif arr[start] > arr[mid]:
            if arr[mid] <= val <= arr[end]:
                return searchInRotatedFrom(mid+1, end)
            else:
                return searchInRotatedFrom(start,mid-1)
        else:
            if arr[mid] == arr[end]:
                return searchInRotatedFrom(start, mid-1) or searchInRotatedFrom(mid+1, end)
            else:
                return searchInRotatedFrom(mid+1, end)

    N = len(arr)

