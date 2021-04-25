def permutation(s1,s2):
    """Given two strings, decide if one is a permutation of the other"""
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)
