import random


def reservoir_sampling(stream,k):
    sample = []
    for id,item in enumerate(stream):
        if id < k:
            sample.append(item)
        elif random.random() < k/(id+1):
            replacement_id = random.randint(0,len(sample)-1)
            sample[replacement_id] = item
    return sample

print(reservoir_sampling([11,13,14,17,19,110],3))

#Timing is Θ(n)