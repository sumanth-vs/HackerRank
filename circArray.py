def circularArrayRotation(a, k, queries):

    for i in range(k % len(a)):
        temp = a[len(a) - 1]
        for j in range(len(a)-1, 0, -1):
            a[j] = a[j-1]
        a[0] = temp

    rotatedArray = []
    for i in queries:
        rotatedArray.append(a[i])
    return rotatedArray


print(circularArrayRotation([1, 2, 3, 4, 5], 12, [0, 1, 2, 3, 4]))
