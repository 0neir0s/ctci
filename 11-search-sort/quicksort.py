def quickSort(arr):
    """ Quick sorting an array """

    def partition(start, end):
        """ Partition array in the given range """
        pivot, index = arr[end], start
        for i in range(start, end):
            if arr[i] <= pivot:
                arr[index], arr[i] = arr[i], arr[index]
                index += 1
        arr[index], arr[end] = arr[end], arr[index]
        print(pivot, arr, index)
        return index

    def quickSortFrom(start, end):
        """ Quick sort from start to end """
        if start >= end:
            return
        index = partition(start, end)
        print(index)
        quickSortFrom(start, index-1)
        quickSortFrom(index+1, end)

    N = len(arr)
    quickSortFrom(0, N-1)

a = [10,7,8,8,11,9]
quickSort(a)
print(a)
