def getTotalX(a, b):
    
    count = 0
    cond1 = []
    flag = False

    #print(min(a))

    for i in range(min(a), max(b) + 1, 1):
        flag = True
        for j in a:
            if i % j != 0 or i < j:
                flag = False
        if flag:
            cond1.append(i)

    for i in cond1:
        flag = True
        for j in b:
            if j % i != 0:
                flag = False
        if flag:
            count += 1
            print(i)

    return count


print(getTotalX([1], [100]))