# code to sort k-lists -non efficient
#
def get_sorted(*combinedlist):
    result = []
    for x in combinedlist:
        y = result
        result = []
        len1,len2 = len(x),len(y)
        i,j = 0,0
        while i < len1 and j < len2:
            if x[i] < y[j]:
                result.append(x[i])
                i += 1
            else:
                result.append(y[j])
                j += 1
        result += x[i:]
        result += y[j:]
    return result

print(get_sorted([1,3,9],[12,16,18],[5,7,11],[4,5,5,6,14,19,25]))
















# def mergesorter(x):
#     if len(x) <= 1:
#         return x
#     mid = len(x)// 2
#     y = mergesorter(x[:mid])
#     z = mergesorter(x[mid:])
#
#     result = []
#     i, j = 0, 0
#     while i < len(y) and j < len(z):
#         if y[i] < z[j]:
#             result.append(y[i])
#             i += 1
#         else:
#             result.append(z[j])
#             j += 1
#     result += y[i:]
#     result += z[j:]
#     return result
#
# print(mergesorter([4,3,6,2,7,4]))