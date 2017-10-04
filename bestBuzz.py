#! /usr/bin/env python
import pickle


# Looks through stored data and picks best combinations of words


# Large word list
adj = ["interoperable", "agile", "mobile", "cloud-based", "scalable", "integrated", "lightweight", "support", "reinforced", "extensible", "maximal", "data-oriented", "distributed", "anomaly-based", "enterprise", "cross-platform", "cross-functional", "deep-learning", "large-scope", "adaptive", "cluster"]
anchor = ["artificial intelligence", "data analytics", "services", "cloud", "virtual reality", "internet of things", "data science", "microservices", "solutions", "development", "blockchain", "machine-learning", "reinforcement learning", "platform"]

# Small test list
#adj = ["interoperable", "agile", "cloud-based", "scalable", "integrated", "lightweight", "reinforced", "extensible", "data-oriented", "anomaly-based", "cross-platform", "adaptive"]
#anchor = ["services", "virtual reality", "internet of things", "microservices", "solutions", "blockchain"]

# Grabbing data from file
dataFile = open(r'data.txt', 'rb')
matrix = pickle.load(dataFile)
dataFile.close()

# making config file
baseReqs = [.15, 0]
cfile = open(r'config.txt', 'wb')
pickle.dump(baseReqs, cfile)
cfile.close()

numRep = 0
totalNum = 0
max = 0
bestX = 0
bestY = 0
bestZ = 0

# NOTE: Diagonal will be blank

for x in range(0, len(matrix)):
    for y in range(0, len(matrix[x])):
        for z in range(0, len(matrix[x][y])):
            numRep += matrix[x][y][z][1]
            totalNum += 1
            if matrix[x][y][z][0] > max:
                max = matrix[x][y][z][0]
                bestX = x
                bestY = y
                bestZ = z

print "Score: " + str(matrix[bestX][bestY][bestZ][0])
print "Number of inputs: " + str(numRep/totalNum)
print "Word: " + adj[bestX] + " " + adj[bestY] + " " + anchor[bestZ]