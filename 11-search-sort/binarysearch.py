
def binarySearch(arr, element):
    """ search an element in a sorted array """
    
    def binarySearchFrom(start, end):
        if start > end:
            return False
        mid = (start+end)//2
        if element == arr[mid]:
            return True
        elif element > arr[mid]:
            return binarySearchFrom(mid+1, end)
        else:
            return binarySearchFrom(0, mid-1)

    return binarySearchFrom(0, len(arr)-1)

print(binarySearch([1,4,6,7], 6))
print(binarySearch([1,4,6,7], 5))

