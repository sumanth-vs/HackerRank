def catAndMouse(x, y, z):
    if abs(z-x) > abs(z-y):
        return "Cat B"
    elif abs(z-x) == abs(z-y):
        return "Mouse C"
    else:
        return "Cat A"
    
print(catAndMouse(1, 3, 2))