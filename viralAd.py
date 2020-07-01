def viralAdvertising(n):
    shared = 5
    liked = 0
    cumul = 0
    for i in range(1, n+1):
        liked = shared // 2
        shared = liked * 3
        cumul += liked

    return cumul

print(viralAdvertising(5))