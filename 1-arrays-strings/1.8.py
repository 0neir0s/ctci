
def isRotation(s1,s2):
    """ Assuming isSubstring is given and can be invoked only once, check if s1 and s2 are rotations. Essentially checking if it is xy and yx form """ 
    return s2 in s1+s1
print(isRotation("waterbottle","erbottlewat"))
