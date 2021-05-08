def allPermutations(s):
    """ return the set of all permutations of a given string """
    if len(s) == 1:
        return {s}
    perms = set()
    ssps = allPermutations(s[1:])
    for ssp in ssps:
        for i in range(len(ssp)+1):
            perms.add(ssp[:i]+s[0]+ssp[i:])
    return perms

print(allPermutations("ssap"))
