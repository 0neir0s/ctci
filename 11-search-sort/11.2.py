from collections import defaultdict
from functools import cmp_to_key

def groupByAnagrams(strings):
    """ sort an array of strings so that all the anagrams are next to each other """
    items = defaultdict(list)
    for text in strings:
        items[''.join(sorted(text))].append(text)
    index = 0
    for anagrams,values in items.items():
        L = len(anagrams)
        strings[index:index+L] = values
        index += L

items = ["fwlj","dbcde","fjlw","were"]
groupByAnagrams(items)
print(items)

def compare(x,y):
    v1, v2 = ''.join(sorted(x)), ''.join(sorted(y))
    if v1 > v2:
        return 1
    elif v1 == v2:
        return 0
    else:
        return -1

def sortModified(strings):
    """ sorting an array of string with anagrams side by side """
    return sorted(strings, key= cmp_to_key(compare))

print(sortModified(["fwlj","dbcde","fjlw","were"]))
