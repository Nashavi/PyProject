from numpy import random, array

def cluster(N,k):
    d=[]
    for i in range(k):
        icenter = random.uniform(10000,100000)
        acenter = random. uniform(20,80)
        for j in range(int(float(N/k))):
            d.append([random.normal(icenter,20000),random.normal(acenter,2)])
    d = array(d)
    return d

from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt

dat = cluster(1000,12)

model = KMeans(n_clusters=12)

model = model.fit(scale(dat))

print model.labels_

plt.scatter(dat[:,0],dat[:,1],c=model.labels_.astype(float))
plt.show()

