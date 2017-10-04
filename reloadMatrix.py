#! /usr/bin/env python
import pickle

# resets data

f = open('data.txt', 'w')
data = []

#adj = ["interoperable", "agile", "cloud-based", "scalable", "integrated", "lightweight", "reinforced", "extensible", "data-oriented", "anomaly-based", "cross-platform", "adaptive"]
#anchor = ["services", "virtual reality", "internet of things", "microservices", "solutions", "blockchain"]

adj = ["interoperable", "agile", "mobile", "cloud-based", "scalable", "integrated", "lightweight", "support", "reinforced", "extensible", "maximal", "data-oriented", "distributed", "anomaly-based", "enterprise", "cross-platform", "cross-functional", "deep-learning", "large-scope", "adaptive", "cluster"]
anchor = ["artificial intelligence", "data analytics", "services", "cloud", "virtual reality", "internet of things", "data science", "microservices", "solutions", "development", "blockchain", "machine-learning", "reinforcement learning", "platform"]

# 3D array, innermost is a tuple that goes (value, numTimesCalled, benchmark)
w, h = len(adj), len(anchor);
matrix = [[[[0, 0, 0] for z in range(h)] for x in range(w)] for y in range(w)]

afile = open(r'data.txt', 'wb')
pickle.dump(matrix, afile)
afile.close()

#reload object from file
file2 = open(r'data.txt', 'rb')
new_d = pickle.load(file2)
file2.close()

# making config file
baseReqs = [.15, 0]
cfile = open(r'config.txt', 'wb')
pickle.dump(baseReqs, cfile)
cfile.close()

#print dictionary object loaded from file
print new_d