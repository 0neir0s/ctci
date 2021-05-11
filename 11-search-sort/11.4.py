# Write the external sort algorithm
# Mocking the actual files with the dictionary.
# File pointers will be a dictionary of file pointers each of which will be replaced with None to avoid StopIteration

from heapq import heapify, heappush, heappop

files = {1: [1,3,5,7], 2: [2,4,6,7], 3: [3,3,8,9], 4: [1,2,9,10]}

heap = []
heapify(heap)

for fn, f in files.items():
    heappush(heap, (f[0], fn))

fps = {1:1, 2:1, 3:1, 4:1}

output = []

while heap:
    minElem, fn = heappop(heap)
    output.append(minElem)
    if fps[fn] < len(files[fn]):
        nxtElem = files[fn][fps[fn]]
        heappush(heap, (nxtElem, fn))
        fps[fn] = fps[fn]+1
print(output)
