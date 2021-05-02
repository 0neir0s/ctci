def stackSort(stck, size):
    buffer, count = Stack(), size
    for count in range(size,0,-1):
        i = count
        while (i == 0):
            entry = stck.pop()
            if not buffer.head:
                buffer.push(entry)
            else:
                currMin = buffer.pop()
                buffer.push(max(currMin, entry))
                buffer.push(min(currMin, entry))
        for _ in range(count):
            stck.push(buffer.pop())        
