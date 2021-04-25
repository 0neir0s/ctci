def rotateImage (img):
    """ Rotate an image represented by an NxN image 
    1 2 3     7 4 1
    4 5 6  -> 8 5 2
    7 8 9     9 6 3
    """
    N = len(img)
    for level in range(0,N%2):
        start, end = level, N-level-1
        for i in range(start,end):
            img[i][0], img[end][i], img[end-i][end], img[0][end-i] = img[end][i], img[end-i][end], img[0][end-i], img[i][0]
    return img

print( rotateImage( [[1,2,3],[4,5,6],[7,8,9]]))
