def countingValleys(n, s):

    level = 0
    inV = 0
    cV = 0

    for i in s:
        if i == 'D':
            level -= 1
            if inV == 0 and level < 0:
                cV += 1
                inV = 1
        else:
            level += 1
            if level >= 0:
                inV = 0

    return cV



n = 8
s = 'DUUDDU'
print(countingValleys(n, s))
