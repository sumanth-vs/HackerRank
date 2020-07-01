def angryProfessor(k, a):
    on_time = 0
    for i in a:
        if i <= 0:
            on_time += 1
    if on_time >= k:
        return 'YES'
    else:
        return 'NO'


print(angryProfessor(5, [-1, -1, 0, 0, 1, 1]))