# Approach 1 - Using in-order and pre-order 

# So substring matching of both the in-orders and pre-orders
# Answer = p2 in p1 and s2 in s1

# Approach 2 - O(mn) O(n + km) - Average would be much lesser due to early stopping

def subTree(n1,n2):
    """ Substring matching - Assumption: n2 is not null """
    if not n1:
        return False
    if matchTree(n1,n2):
        return True
    return subTree(n1.left, n2) or subTree(n1.right, n2)

def matchTree(n1,n2):
    """ Comparison function - recursive """
    if not n1 and not n2:
        return True
    if not n1 or not n2:
        return False
    if n1.data != n2.data:
        return False
    return matchTree(n1.left, n2.left) and matchTree(n1.right, n2.right)
