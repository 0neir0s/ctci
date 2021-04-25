# Implement an algorithm to determine if a string has all unique characters

s = "blahblah"

def isUnique (s):
    return len(set(s)) == len(s)
