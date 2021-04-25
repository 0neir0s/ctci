def compressor (text):
    """ A method to perform basic string compression using the counts of repeated characters f: aabcccccaaa -> a2b1c5a3, if compressed is not smaller, return the original string """
    chList, i = [], 0
    while (i < len(text)):
        count,i,ch = 1,i+1,text[i]
        while ( i < len(text) and ch == text[i] ):
            count, i = count+1, i+1
        chList.append(ch+str(count))
    compressed = ''.join(chList)
    return compressed if len(compressed)<len(text) else text

print(compressor("aabcccccaaa"))

