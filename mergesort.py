list2 = [ 4,7,14,66,86,92,165,354,678]
list1 = [1,2,5,8,10,14,7,4,6,9,5]

def mergersorter(x) :
    result = []
    if len(x) <= 1:
        return x
    mid = int(len(x)/2)
    firsth = x[:mid]
    secondh = x[mid:]
    y = mergersorter(firsth)
    z = mergersorter(secondh)
    i,j = 0,0
    len1,len2 = len(y),len(z)
    while i <len1 and j < len2:
        if y[i] < z[j]:
            result.append(y[i])
            i +=1
        else:
            result.append(z[j])
            j +=1
    result += y[i:]
    result += z[j:]
    return result

print(mergersorter(list1))