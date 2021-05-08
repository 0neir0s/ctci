def allParenthesis(n):
    """ Print all combinations of n-pairs of parentheses """
    
    def getAllParenthesis(n):
        """ get the set of all valid parentheses """
        if n == 1:
            return {"()"}
        output = set()
        for sOutput in getAllParenthesis(n-1):
            for loc in range(len(sOutput)+1):
                output.add(sOutput[:loc]+"()"+sOutput[loc:])
        return output
    
    for i in getAllParenthesis(n):
        print(i)

#allParenthesis(4)

def allParenthesesV2(n):
    """ get the set of all valid parenthesis by avoiding duplications """
    def getAllParentheses(lp, rp, pos):
        """ build the strings from scratch and when completed, add to the list """
        if lp == 0:
            builderString[pos:] = [")"]*rp
            validStrings.append(''.join(builderString))
            return
        if lp == rp:
            builderString[pos] = "("
            getAllParentheses(lp-1,rp,pos+1)
            return
        builderString[pos] = "("
        getAllParentheses(lp-1,rp,pos+1)
        builderString[pos] = ")"
        getAllParentheses(lp,rp-1,pos+1)

    validStrings = []
    builderString = [""]*2*n
    getAllParentheses(n,n,0)
    return validStrings

print(allParenthesesV2(3))
