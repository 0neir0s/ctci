from functools import cache

def paintFill(screen, newColor, point):
    """ Given a point, color and the screen, fill the screen with color """
    @cache
    def painter(x,y):
        if not (0 <= x < M) or not (0 <= y < N):
            return
        if screen[x][y] != color:
            return
        screen[x][y] = newColor
        for nx,ny in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
            painter(nx,ny)

    M, N = len(screen), len(screen[0])
    x, y = point
    if screen[x][y] == newColor:
        return
    color = screen[x][y]
    painter(x,y)

screen = [[2,1,3,4],[1,1,1,1],[3,4,5,6]]
paintFill(screen, 2, (1,2))
print(screen)
