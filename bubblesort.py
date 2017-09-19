def bubblesort(x):
    if len(x) < 2:
        return x
    i = 1
    while i < len(x):
        while x[i-1] > x[i] and i > 0:
            x[i],x[i-1] = x[i-1],x[i]
            i -= 1
        i += 1
    return x


print(bubblesort([2,4,1,3,7,5,4,6,9,3,1,5]))