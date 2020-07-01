# def saveThePrisoner(n, m, s):
#     i = s
#     candyDistr = 0
#     while candyDistr < m:
#         candyDistr += 1
#         if i == n and candyDistr != m:
#             i = 1
#             continue
#         i += 1

#     return i-1


# alternate way

def saveThePrisoner(n, m, s):
    if m < n:
        return m
    else:
        return (m - (n-s+1)) % n


print(saveThePrisoner(5, 2, 2))


