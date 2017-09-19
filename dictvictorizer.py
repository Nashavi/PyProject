from sklearn.feature_extraction import DictVectorizer

v = DictVectorizer(sparse=False)

df = [{'a': 1, 'c': 2}, {'c': 3, 'e': 1},{'b':5},{'d': 3,'e': 2},{'a':2,'b' : 5, 'c' : 3, 'd' : 7}]

x = v.fit_transform(df)

print(x)
