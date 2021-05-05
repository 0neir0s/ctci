def fractionToBinary(frac):
    """ Transform a double b/w 0 and 1 to a binary fraction """
    a, i = [], 0
    while i < 31:
        i += 1
        frac *= 2
        a.append(str(int(frac)))
        frac -= int(frac)
        if frac == 0:
            break
    if i == 31:
        print("ERROR")
        return
    print(".{}".format(''.join(a)))

if __name__ == "__main__":
    fractionToBinary(0.125)
