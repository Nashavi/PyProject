def bubblesort(x):
    for i in range(len(x)):
        for j in range(len(x) - 1 -i):
            if x[j] > x[j+1]:
                x[j],x[j+1] = x[j+1],x[j]
            print(x)
    print(x)
    
print(bubblesort([2,4,1,3,7,5,4,6,9,3,1,5]))
