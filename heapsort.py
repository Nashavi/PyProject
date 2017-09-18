def heapsort(items):
    import heapq
    h = []
    for item in items:
        heapq.heappush(h,item)
    return [heapq.heappop(h) for k in range(len(h))]

print(heapsort([5,3,1,4,6,9,8]))