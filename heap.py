import heapq

def mergeKArray(*lists):
    # implemented by min heap
    h = []
    r = []
    for k, arr in enumerate(lists):
        heapq.heappush(h, (arr[0], 0, k))
    print(h)
    print()
    while h:
        # min is the minimum element
        # i is the index of the min in the k-th array
        # k is the index of array in the list
        min, i, k = heapq.heappop(h)
        r.append(min)
        if i < len(lists[k]) - 1:
            i += 1
            heapq.heappush(h, (lists[k][i], i, k))
        print(h)
    return r

print(mergeKArray([1,3,9],[12,16,18],[5,7,11],[4,5,5,6,14,19,25]))