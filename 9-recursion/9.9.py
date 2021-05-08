
def queensArrangement(n):
    """ Print all ways of arranging n queens on a chess board """
    def canPlace(row, col):
        for loc in locations:
            if not loc:
                break
            r,c = loc
            status = (row==r) or (col==c) or ((row-col) == (r-c)) or ((row+col) == (r+c))
            if status:
                return False
        return True

    def dfs(row):
        """ valid arrangements finder """
        if row == n:
            arrangements.append(locations)
            return
        for col in range(n):
            if not canPlace(row,col):
                continue
            locations[row] = (row,col)
            dfs(row+1)
            locations[row] = None

    arrangements = []
    locations = [None]*n
    for c in range(n):
        locations[0] = (0,c)
        dfs(1)
    return arrangements

print(len(queensArrangement(8)))
