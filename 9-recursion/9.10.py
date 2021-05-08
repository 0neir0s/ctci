from functools import cache

def canStack(bottom, top):
    """ returns if top can be stacked on bottom"""
    bw, bh, bd = bottom
    tw, th, td = top
    return (bw < tw) and (bh < th) and (bd < td)

def getStackCount(boxes):
    """ given a list of boxes, find the tallest stack """
    @cache
    def getStackCountWith(b):
        """ get the count of stack boxes with box as the bottom """
        options = [t for t in boxes if canStack(b,t)]
        _,height,_ = b
        if not options:
            return height
        return height + max(getStackCountWith(t) for t in options)
    return max(getStackCountWith(box) for box in boxes)

boxes = [(5,4,5), (3,8,3), (1,2,2), (6,6,6)]
print(getStackCount(boxes))
