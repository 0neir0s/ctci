def allSubsets(elems):
    """ return the set of all subsets of elems """
    l = len(elems)
    if l == 0:
        return []
    if l == 1:
        return [set(),set(elems)]
    if l == 2:
        return [set(),set(elems),{elems[0]},{elems[1]}]
    output = []
    for ss in allSubsets(elems[1:]):
        output.append(ss)
        output.append(ss.union({elems[0]}))
    return output

print(allSubsets([1,2,3,4]))
