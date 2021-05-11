from collections import defaultdict

def countingSort(arr, getter, numRange):
    arranged = defaultdict(list)
    for i in arr:
        arranged[getter(i)].append(i)
    output = []
    for order in numRange:
        output.extend(arranged[order])
    for i, elem in enumerate(output):
        arr[i] = elem

def radixSort(arr):
    digits = len(str(max(arr)))
    for i in range(digits):
        countingSort(arr, lambda x: (x // 10**i)%10, range(0,10))

a = [10,23,12,802,12]
radixSort(a)
print(a)
