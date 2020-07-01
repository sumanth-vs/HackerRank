def beautifulDays(i, j, k):
    count = 0
    for i in range(i, j+1):
        diff = abs(i - int(str(i)[::-1]))
        if diff % k == 0:
            count += 1

    return count


print(beautifulDays(20, 23, 6))