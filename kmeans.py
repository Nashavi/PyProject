from numpy import random, array

def createcluster(N,k) :
    random.seed(10)
    pointspercluster = float(N/k)
    x = []
    for i in range (k):
        incomecenter=random.uniform(20000,200000)
        agecentroid=random.uniform(20,70)
        for j in range(int(pointspercluster)):
            x.append([random.normal(incomecenter,10000), random.normal(agecentroid,2)])
    x= array(x)
    return x


from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale

data = createcluster(100,7)

model = KMeans(n_clusters=7)

model= model.fit(scale(data))

print model.labels_

plt.figure(figsize=(8,6))
plt.scatter(data[:,0],data[:,1],c=model.labels_.astype(float))
plt.show()